import requests
from typing import Optional, Dict, Any

class SafeCommsClient:
    def __init__(self, api_key: str, base_url: str = "https://safecomms.dev/api/v1/public"):
        self.api_key = api_key
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        })

    def moderate_text(self, content: str, language: str = "en", replace: bool = False, pii: bool = False, replace_severity: Optional[str] = None, moderation_profile_id: Optional[str] = None) -> Dict[str, Any]:
        """
        Moderate text content.
        """
        payload = {
            "content": content,
            "language": language,
            "replace": replace,
            "pii": pii,
            "replaceSeverity": replace_severity,
            "moderationProfileId": moderation_profile_id
        }
        response = self.session.post(f"{self.base_url}/moderation/text", json=payload)
        response.raise_for_status()
        return response.json()

    def get_usage(self) -> Dict[str, Any]:
        """
        Get current usage statistics.
        """
        response = self.session.get(f"{self.base_url}/usage")
        response.raise_for_status()
        return response.json()
