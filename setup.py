from setuptools import setup, find_packages

if __name__ == "__main__":
    setup(
        name = 'examplepackage',
        version = 0.1,
        author = 'Simon Heise',
        author_email = '',
        url = 'https://github.com/nomispaz/swayautotile/',
        description = 'Simple Autotile skript for sway (and possibly i3)',
        long_description_content_type = "text/x-rst",  # If this causes a warning, upgrade your setuptools package
        long_description = '',
        license = "MIT license",
        packages = find_packages(exclude=["test"]),  # Don't include test directory in binary distribution
        install_requires = i3ipc,
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ]
    )
