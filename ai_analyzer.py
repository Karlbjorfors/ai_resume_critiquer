from openai import OpenAI
from typing import Optional

class ResumeAnalyser:
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)

    def analyze_resume(self, resume_content: str, job_role: Optional[str] = None) -> str:
        """Analyze the resume content and provide feedback."""
        prompt = self._build_prompt(resume_content, job_role)
        
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an expert resume reviewer with years of experience in HR and recruitment."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500
        )
        return response.choices[0].message.content
    
    def _build_prompt(self, resume_content: str, job_role: Optional[str]) -> str:
        """Build the analysis prompt."""
        job_specific = job_role if job_role else "general job applications"

        return f"""Please analyze this resume and provide constructive feedback.
        Focus on the following aspects:
        1. Content clarity and impact
        2. Skills presentation
        3. Experience descriptions
        4. Specific improvements for {job_specific}

        Resume content:
        {resume_content}

        Please provide your analysis in a clear, structured format with specific recommendations"""