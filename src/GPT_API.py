from google import genai 

class GeminiClient:
    def __init__(self):
        _api_key = "api_key"
        self.model = "gemini-2.0-flash"
        self.client = genai.Client(api_key=_api_key)

    def get_response(self, prompt: str, dump_json: bool = False) -> str:
        
        try:
            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt
                )
            if not response.text:
                raise ValueError("Gemini API returned empty response")
            if dump_json:
                return response.text,response.model_dump_json(
                        exclude_none=True, indent=4)
            return response.text
                
        except Exception as e:
            raise AttributeError(f"Gemini API Error: {str(e)}")
