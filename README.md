# Streamlit Media App

A Streamlit application for displaying images and videos.

## Setup with Conda

### Prerequisites

- Anaconda or Miniconda installed on your system

### Installation Steps

1. **Create the conda environment from the environment.yml file:**

   ```bash
   conda env create -f environment.yml
   ```

2. **Activate the environment:**

   ```bash
   conda activate streamlit-media-app
   ```

3. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

### Alternative Manual Setup

If you prefer to create the environment manually:

```bash
# Create a new conda environment
conda create -n streamlit-media-app python=3.9

# Activate the environment
conda activate streamlit-media-app

# Install required packages
conda install -c conda-forge streamlit pillow

# Run the app
streamlit run app.py
```

## Usage

Once the app is running, it will open in your default web browser at `http://localhost:8501`. The app displays:

- A logo image
- A banner GIF
- Image galleries in columns
- Video content

## File Structure

```
streamlit-media-app/
├── app.py                 # Main Streamlit application
├── environment.yml        # Conda environment configuration
├── assets/               # Media assets directory
│   ├── videos/          # Video and image files
│   └── Icon-colored-nobg.png
└── README.md            # This file
```

## Troubleshooting

- If you encounter issues with missing files, ensure all referenced media files exist in the `assets/` directory
- Make sure the conda environment is activated before running the app
- If packages are missing, reinstall using: `conda env update -f environment.yml`
