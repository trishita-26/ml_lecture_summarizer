
# ML Lecture Summarizer

## Overview

ML Lecture Summarizer is an end-to-end machine learning project that converts lecture audio files into concise summaries. It also extracts key topics and generates quizzes to enhance learning retention. The project uses state-of-the-art NLP models for transcription, summarization, keyword extraction, and quiz generation.

---

## Features

- Transcribes lecture audio into text using speech-to-text models
- Summarizes lengthy lecture transcripts into digestible summaries
- Extracts important keywords and topics from transcripts
- Generates quiz questions based on lecture content
- Interactive frontend using Streamlit for easy user access

---

## Project Structure

```

ml\_lecture\_summarizer/
│
├── data/
│   └── raw\_lectures/           # Input folder for lecture audio files (mp3, wav, etc.)
├── models/                     # ML model scripts
│   ├── summarizer.py           # Text summarization logic
│   ├── keyword\_extractor.py    # Keyword extraction logic
│   └── quiz\_generator.py       # Quiz generation logic
├── utils/                      # Helper utilities
│   ├── cleaner.py              # Text cleaning functions
│   └── audio\_to\_text.py        # Audio transcription functions
├── app/
│   └── streamlit\_app.py        # Streamlit frontend app
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
└── demo/                      # Demo assets like video walkthrough
└── demo\_video.mp4

````

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/trishita-26/ml_lecture_summarizer.git
cd ml_lecture_summarizer
````

2. Create and activate a virtual environment (optional but recommended):

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

1. Place your lecture audio files (MP3, WAV, etc.) inside the `data/raw_lectures/` folder.

2. Run the Streamlit app:

```bash
streamlit run app/streamlit_app.py
```

3. Open the provided local URL in your browser to upload lectures and get summaries, keywords, and quizzes.

---

## Contributing

Contributions are welcome! Please open issues or pull requests to suggest improvements or fixes.

---

## License

This project is licensed under the MIT License.

---

## Contact

Created by Trisita — feel free to reach out via GitHub for questions or collaborations.

```

---

