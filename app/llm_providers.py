from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Callable

from dotenv import load_dotenv


load_dotenv()


TEMPLATE_ONLY = "Template only"
PROVIDER_OPENAI = "OpenAI"
PROVIDER_GEMINI = "Gemini"
PROVIDER_OPENROUTER = "OpenRouter"


SYSTEM_INSTRUCTIONS = """
You are a Product Management review assistant.

You do not own product decisions.
You do not invent facts.
You do not convert uncertainty into certainty.
You do not pretend unresolved questions are solved.

Your job is to review a generated PM artifact and identify:

1. missing product decisions;
2. unclear assumptions;
3. weak acceptance criteria;
4. scope risks;
5. technical dependencies;
6. data ownership questions;
7. legal or compliance questions;
8. follow-up discovery questions.

Separate your output into clear sections.

Use concise, practical, product-management language.

If something is unresolved, label it as:
- Missing decision;
- Needs validation;
- Scope risk;
- Technical dependency;
- Legal/compliance question;
- Stakeholder alignment issue.

Do not rewrite the whole artifact unless explicitly asked.
"""


@dataclass(frozen=True)
class LLMProviderConfig:
    name: str
    env_key: str
    model_env_key: str
    default_model: str


PROVIDER_CONFIGS: dict[str, LLMProviderConfig] = {
    PROVIDER_OPENAI: LLMProviderConfig(
        name=PROVIDER_OPENAI,
        env_key="OPENAI_API_KEY",
        model_env_key="OPENAI_MODEL",
        default_model="gpt-5.5",
    ),
    PROVIDER_GEMINI: LLMProviderConfig(
        name=PROVIDER_GEMINI,
        env_key="GEMINI_API_KEY",
        model_env_key="GEMINI_MODEL",
        default_model="gemini-2.5-flash",
    ),
    PROVIDER_OPENROUTER: LLMProviderConfig(
        name=PROVIDER_OPENROUTER,
        env_key="OPENROUTER_API_KEY",
        model_env_key="OPENROUTER_MODEL",
        default_model="openrouter/auto",
    ),
}


def get_api_key(provider: str) -> str | None:
    config = PROVIDER_CONFIGS.get(provider)
    if not config:
        return None

    value = os.getenv(config.env_key, "").strip()
    return value or None


def get_model(provider: str) -> str:
    config = PROVIDER_CONFIGS[provider]
    return os.getenv(config.model_env_key, config.default_model).strip() or config.default_model


def provider_is_configured(provider: str) -> bool:
    if provider == TEMPLATE_ONLY:
        return True
    return get_api_key(provider) is not None


def get_available_providers() -> list[str]:
    providers = [TEMPLATE_ONLY]

    for provider in [PROVIDER_GEMINI, PROVIDER_OPENROUTER, PROVIDER_OPENAI]:
        if provider_is_configured(provider):
            providers.append(provider)

    return providers


def get_provider_status() -> dict[str, bool]:
    return {
        TEMPLATE_ONLY: True,
        PROVIDER_GEMINI: provider_is_configured(PROVIDER_GEMINI),
        PROVIDER_OPENROUTER: provider_is_configured(PROVIDER_OPENROUTER),
        PROVIDER_OPENAI: provider_is_configured(PROVIDER_OPENAI),
    }


def build_review_prompt(markdown_artifact: str) -> str:
    return f"""
Review the following generated PM artifact.

Focus on product-management quality.

Return:

1. Missing product decisions
2. Unclear assumptions
3. Weak acceptance criteria
4. Scope risks
5. Technical dependencies
6. Data ownership questions
7. Legal/compliance questions
8. Follow-up discovery questions
9. Top 5 recommended improvements

Generated artifact:

{markdown_artifact}
"""


def review_with_openai(markdown_artifact: str) -> str:
    from openai import OpenAI

    api_key = get_api_key(PROVIDER_OPENAI)
    if not api_key:
        return "OpenAI is not configured. Set OPENAI_API_KEY to enable this provider."

    client = OpenAI(api_key=api_key)
    model = get_model(PROVIDER_OPENAI)

    response = client.responses.create(
        model=model,
        instructions=SYSTEM_INSTRUCTIONS,
        input=build_review_prompt(markdown_artifact),
    )

    return getattr(response, "output_text", "") or str(response)


def review_with_gemini(markdown_artifact: str) -> str:
    from google import genai

    api_key = get_api_key(PROVIDER_GEMINI)
    if not api_key:
        return "Gemini is not configured. Set GEMINI_API_KEY to enable this provider."

    client = genai.Client(api_key=api_key)
    model = get_model(PROVIDER_GEMINI)

    prompt = f"{SYSTEM_INSTRUCTIONS}\n\n{build_review_prompt(markdown_artifact)}"

    response = client.models.generate_content(
        model=model,
        contents=prompt,
    )

    return getattr(response, "text", "") or str(response)


def review_with_openrouter(markdown_artifact: str) -> str:
    from openai import OpenAI

    api_key = get_api_key(PROVIDER_OPENROUTER)
    if not api_key:
        return "OpenRouter is not configured. Set OPENROUTER_API_KEY to enable this provider."

    client = OpenAI(
        api_key=api_key,
        base_url="https://openrouter.ai/api/v1",
    )

    model = get_model(PROVIDER_OPENROUTER)

    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": SYSTEM_INSTRUCTIONS},
            {"role": "user", "content": build_review_prompt(markdown_artifact)},
        ],
    )

    if not completion.choices:
        return "OpenRouter returned no choices."

    return completion.choices[0].message.content or ""


REVIEW_FUNCTIONS: dict[str, Callable[[str], str]] = {
    PROVIDER_OPENAI: review_with_openai,
    PROVIDER_GEMINI: review_with_gemini,
    PROVIDER_OPENROUTER: review_with_openrouter,
}


def review_artifact(provider: str, markdown_artifact: str) -> str:
    if provider == TEMPLATE_ONLY:
        return (
            "Template-only mode is active. "
            "Set GEMINI_API_KEY, OPENROUTER_API_KEY, or OPENAI_API_KEY to enable LLM review."
        )

    if provider not in REVIEW_FUNCTIONS:
        return f"Unknown provider: {provider}"

    if not provider_is_configured(provider):
        return f"{provider} is not configured. Add the relevant API key to your environment or .env file."

    return REVIEW_FUNCTIONS[provider](markdown_artifact)
