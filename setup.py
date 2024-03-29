from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# edit below variable as per your requirement
REPO_NAME = "Spotify Recommendation System"
AUTHOR_NAME = "Bhor Santosh"
SRC_REPO = "music_recommend"
LIST_OF_REQUIREMENTS = []

setup(
    name=REPO_NAME,
    version="1.0.0",
    author=AUTHOR_NAME,
    author_email="<EMAIL>",
    description="Recommendation System for Music",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BhorSantosh/Spotify-recommendation-system",
    project_urls={
        "Bug Tracker": "https://github.com/BhorSantosh/Spotify-recommendation-system/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Mathematics"
    ]
    ,
    python_requires=">=3.6",
    install_requires=LIST_OF_REQUIREMENTS,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    entry_points={
        "console_scripts": [
            "spotify-recommendation-system=src.music_recommend.main:main",
        ]
        ,
        "gui_scripts": [
            "spotify-recommendation-system-gui=src.music_recommend.app:main",
        ]
    }
)