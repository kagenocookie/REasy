[![Build and Package REasy](https://github.com/seifhassine/REasy/actions/workflows/build.yml/badge.svg)](https://github.com/seifhassine/REasy/actions/workflows/build.yml)
# REasy Editor v0.3.7

<p align="center">
  <img src="resources/images/reasy_editor_logo.png" alt="REasy Editor Logo" style="max-width:300px;">
</p>


<br>

**REasy Editor** is a quality-of-life toolkit for RE games that currently supports viewing and editing of some RE Engine files. It also includes miscellaneous tools to speed up your work. 
Supports RSZ files (SCN, PFB, User) from all games, as well as UVAR, MSG files.


<br>
<br>

<p align="center">
   <img src="https://github.com/user-attachments/assets/64a84918-ad58-47ee-8186-e0e7a5a1ace0" alt="REasy Editor Logo" width=70%">
</p>

<br>


## Features

<br>
<div align="center">
  
| File Type | Viewing | Editing | Tested On |
|-----------|---------|---------|-----------|
| UVAR      | ✅       | ✅       | RE4, RE2  |
| RCOL (temporarily disabled)      | ❌       | ❌       | RE4       |
| SCN       | ✅       | ✅       | Most titles       |
| User       | ✅       | ✅       |Most titles       |
| PFB       | ✅       | ✅       | Most titles      |
| MSG       | ✅       | ✅       | RE4      |
| EFX       | Coming Soon       | Coming Soon       |       |
  
</div>
<br>
<br>

- **UVAR File Editing:**  
  - View and fully modify UVAR files. Hashing and mapping are taken care of automatically.
  - Add new variables with automatic naming that preserves numeric formatting (e.g. "Location47_031" followed by "Location47_032").
  This allows you to add new flags to RE4R for example (which was not possible with existing tools).
  - Deletion of variables is also supported.
  
- **RSZ File Viewing and Editing:**  
  - User, PFB and SCN files are supported with advanced editing.
  - GameObjects and Array Elements are fully serializaible into JSON.
  - You can export and import GameObjects in RSZ files through REasy using the Template Manager. Exported GameObjects can be found in the "templates" directory in plaintext (JSON).  

- **Search Functionality:**  
  Search all files across directories for:
  - Specific text (UTF-16LE encoded)
  - 32-bit numbers (with hexadecimal display)
  - GUIDs (with conversion from standard format)

- **GUID Converter Tool:**  
  Convert between memory (hyphenated hex) and standard (hyphenated) GUID formats.

- **Dark Mode:**  
  Toggle a dark mode theme that applies to all dialogs and windows.



## Unique Use-Cases:

- **Adding New Flags to RE4R:**  
  I tested adding 22000 new flags (file size went from 2mb to ~16mb), and tried some of them randomly. Game was stable. At 50k added flags, it crashes when a gamesave is triggered. To determine the exact threshold, your testing and feedback are needed. But 20k should be more than enough. (I wrote a guide [here](https://www.nexusmods.com/residentevil42023/articles/346))
  
- **Finding all files where some data is referenced:**
  Ever encountered a flag but don't know in which file it is set? This tool allows you to find all locations where that flag is checked/set.

## Correctness

- All RSZ (.user, .pfb, .scn) files from most games have been fully tested (read then re-written, producing the same data as original file).

## RSZ Dumps:

- Under [/resources/data/dumps](https://github.com/seifhassine/REasy/tree/master/resources/data/dumps) you will find a list of updated RSZ templates for all games. 

## Installation

- Run build.bat

- Dependencies in requirements.txt

## Credits:

@alphazolam for the uvar template.

@TrikzMe for RE's MurMurHash3 

@praydog, for making the RSZ JSON dumps and REF. 

@don on Discord for helping out with .exe debugging related stuff.

@shadowcookie for consulting with misc. stuff

## Support REasy:

If you appreciate my work and would like to support the development of the tool, you can support me through this [link](https://linktr.ee/seifhassine)

## License, Contributions:

REasy is under MIT license.
You are wlecome to contribute to the project. I am currently active and will review PRs.

