<div style="display:flex; align-items:center;">
    <img align="left" alt="Saldine Icon" src="https://github.com/nautrw/saldine/assets/160557714/7761b9b5-b767-4e9a-8d54-207992f4c180" width="50%">
    <p align="right">Saldine is a sheet music generation algorithm for the terminal. It uses probability and rules to preform mathematical equations and generate musical notes for sheet music.
</div>

## How it works
The program works in the following steps. Terms such as *steps* and *intervals* will not be explained here.
1. The user is asked for the number of notes and if the program should add a whole note at the end. Should the user chose to add a whole note, it will subtract 1 from the number of notes, so as to accomodate for the whole note. The program will subtract 1 from the number of notes again so as to accomodate for the next step.
1. A starting note is chosen. This note can be any of the 7 possible notes and of any of the possible lengths. As of right now, it is just a number corresponding to a note.
1. An interval is chosen based on the previous note. There are 4 possible intervals. A step interval has a probability of `50%`. An unison interval has a probability of `25%`. A skip interval has a probability of `22.5%` in total. There are different types of skips. A third skip has a `11.5%` chance of being chosen. A sixth skip has a `4.5%` chance of being chosen. A fifth skip interval has a `4.5%` chance of being chosen. A fourth skip interval has a `2.25%` chance of being chosen. A full octave interval has a probability of being chosen `2.5%` of the time. The interval is then transformed into a mathematical operation which will be performed on the number of the previous note. Every step leads to another step in this program.
1. A note length is chosen as well. A whole note has a `2.5%` chance of being chosen. A half note has a `12.5%` chance. A dotted half note has a `10%` chance. A quarter note has a `62.5%` chance. An eighth note has a `12.5%` chance of being chosen. The note length is not dependent on anything else. The program does not take into account the time signature.
1. All of these notes generated are added into a list which is then passed through the parser. The parser maps out every note number to their corresponding note and color. It also unites the note names and lengths into the custom notation used in the program. See [the notation](#the-notation) for more details.

## The Notation
I have designed the notation of the program to be easily read.

### The format
The format of each note is as following:
```
[Note Name]{Abbreviation of the length}
```
The note names are as-is and should be intuitive. The program was designed for the C scale, and thus it was tested with the C scale. Other scales have not been tested very much, though you are welcome to try!

### Note lengths
The note lengths in the program are abbreviations of the actual names. The following is a chart explaining it.

|Abbreviation|Meaning|
|------------|-------|
|`WH`|Whole Note|
|`HA`|Half Note|
|`DQ`|Dotted Quarter Note|
|`QU`|Quarter Note|
|`EI`|Eighth Note|

## Screenshots
![Example of Saldine #1](https://github.com/nautrw/saldine/assets/160557714/c3cd5175-3428-4798-86d1-970012b4e1ad)
![Example of Saldine #2](https://github.com/nautrw/saldine/assets/160557714/008b0bb6-7ec0-4d00-bd7d-715d215499bf)
![Example of Saldine #3](https://github.com/nautrw/saldine/assets/160557714/3d66dd85-7922-496d-bfc3-ba9fd2a15d31)
