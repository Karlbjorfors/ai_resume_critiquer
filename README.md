# Project2 - AI Resume Critiquer

An intelligent resume analysis tool built with Streamlit and OpenAI that provides personalized feedback to help you improve your resume for specific job applications.

## 🚀 Features

- **Resume Upload Support**: Accepts both PDF and TXT file formats
- **AI-Powered Analysis**: Uses OpenAI's GPT-4o-mini model for intelligent resume critique
- **Job-Specific Feedback**: Tailors recommendations based on the target job role
- **Interactive Web Interface**: Clean, user-friendly Streamlit interface
- **Comprehensive Analysis**: Covers content clarity, skills presentation, experience descriptions, and targeted improvements

## 🛠️ Technologies Used

- **Streamlit**: Web application framework for the user interface
- **OpenAI GPT-4o-mini**: Advanced language model for resume analysis
- **PyPDF2**: PDF text extraction library
- **Python**: Core programming language
- **python-dotenv**: Environment variable management

## 📋 Prerequisites

- Python 3.11+
- OpenAI API key with available credits [Get it](https://platform.openai.com/)
- Git (for cloning)
- **uv** (recommended for dependency management) - [Installation guide](https://docs.astral.sh/uv/getting-started/installation/)

### Installing uv

**Windows (PowerShell):**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**macOS and Linux:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Using pip:**

```bash
pip install uv
```

**Using pipx:**

```bash
pipx install uv
```

For more installation options and troubleshooting, visit the [official uv installation guide](https://docs.astral.sh/uv/getting-started/installation/).

## 🔧 Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Karlbjorfors/ai_resume_critiquer.git
   cd ai-resume-critiquer
   ```

2. **Install dependencies using uv (recommended)**

   ```bash
   uv sync
   ```

   Or with pip:

   ```bash
   pip install streamlit openai pypdf2 python-dotenv
   ```

3. **Set up environment variables**

   ```bash
   # Create .env file and add your OpenAI API key
   echo "OPENAI_API_KEY=your_api_key_here" > .env
   ```

## 🚀 Usage

1. **Start the Streamlit application**

   ```bash
   uv run streamlit run main.py
   ```

2. **Use the application**
   - Open your browser to `http://localhost:8501`
   - Upload your resume (PDF or TXT format)
   - Optionally enter the job role you're applying for
   - Click "Analyze Resume" to get AI-powered feedback

## 📊 Analysis Features

The AI Resume Critiquer provides feedback on:

### Content Clarity and Impact

- Overall readability and structure
- Effectiveness of content presentation
- Professional language usage

### Skills Presentation

- Technical and soft skills organization
- Relevance to target positions
- Skills gap identification

### Experience Descriptions

- Achievement quantification
- Action verb usage
- Impact demonstration

### Job-Specific Improvements

- Tailored recommendations for target roles
- Industry-specific suggestions
- Keyword optimization advice

## 📁 Project Structure

```
project2/
├── main.py              # Main Streamlit application (UI only)
├── resume_processor.py  # File handling and text extraction
├── ai_analyzer.py       # OpenAI integration and analysis
├── pyproject.toml       # Project dependencies and metadata
├── .env                 # Environment variables (not in git)
├── .gitignore          # Git ignore rules
├── .python-version     # Python version specification
├── uv.lock             # Dependency lock file
└── README.md           # This file
```

## 🏗️ Code Architecture

The application follows a clean separation of concerns:

- **`main.py`**: Streamlit UI components and user interaction flow
- **`resume_processor.py`**: File upload handling, text extraction from PDF/TXT files
- **`ai_analyzer.py`**: OpenAI client initialization and resume analysis logic

This modular structure makes the code:

- Easy to maintain and extend
- Simple to test individual components
- Clear separation between UI and business logic

## 🔒 Security & Privacy

- **API Key Protection**: Your OpenAI API key is stored locally in `.env` file
- **No Data Storage**: Resume content is processed in real-time, not stored
- **Secure Processing**: All communication with OpenAI API is encrypted
- **Local Processing**: File parsing happens locally on your machine

## ⚙️ Configuration

### Environment Variables

Create a `.env` file with:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

### Streamlit Configuration

The app is configured with:

- Page title: "AI Resume Critiquer"
- Page icon: 📄
- Layout: Centered
- File upload types: PDF, TXT

## 🐛 Troubleshooting

### Common Issues

1. **"You exceeded your current quota"**

   - Check your OpenAI billing at [OpenAI Platform](https://platform.openai.com/usage)
   - Ensure sufficient API credits

2. **File upload errors**

   - Verify file is in PDF or TXT format
   - Check file size (Streamlit has default limits)
   - Ensure file contains readable text

3. **PDF extraction issues**

   - Some PDFs may have text as images (not extractable)
   - Try converting to TXT format
   - Ensure PDF is not password-protected

4. **Import errors**
   - Install dependencies: `uv sync` or `pip install -r requirements.txt`
   - Check Python version: 3.11+

## 🔄 Development

### Running in Development Mode

```bash
# Install development dependencies
uv sync

# Run with auto-reload
streamlit run main.py --server.runOnSave true
```

### Adding New Features

The modular codebase makes it easy to add new features:

1. **New file types**: Extend `resume_processor.py` with additional extraction methods
2. **Enhanced analysis**: Modify the prompt in `ai_analyzer.py` or add new analysis methods
3. **UI improvements**: Update `main.py` for new user interface elements
4. **New AI models**: Easily swap models in the `ResumeAnalyzer` class

## 📈 Future Enhancements

- [ ] Support for DOCX files
- [ ] Resume scoring system
- [ ] Export analysis results to PDF
- [ ] Multiple language support
- [ ] Resume template suggestions

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

---

⭐ If you found this project helpful, please give it a star!

## 🙏 Acknowledgments

- OpenAI for providing the GPT-4o-mini API
- Streamlit team for the excellent web framework
- PyPDF2 contributors for PDF processing capabilities
