# Smart acdamic expense tracker

## Overview
a moduler python python cli application built to satisfy course project requirements.

## Features
- moduler object-oriented architecture (classes,encapsulation)
- cli menu navigation with input validation 
array and dictionary structures for catrgorical data aggregation
- local json data presistence (`data/expenses.json`)

## Directory Structure
```text
SMART EXPENSE TRACKER/
|--data/
|   |__expenses.json
|
|--engine/                       
|   |-- __init__.py
|   |__ tracker.py
|
|--models/
|   |-- __init__.py
|   |__ expense.py
|
|--utils/
|   |-- __init__.py
|   |__ validators.py
|
|--main.py
|--readme.md
|__statement.md

## Key points
the smart academic expense tracker is a terminal based python application designed speacifically to help university students manage,catagorize,and analyze their everyday educational and living expenses

instead of dealing with clutted spreadsheets or keeping manual notes , students can use this tool to log speciifc costs associated with university life-such as textbooks,tuition fees,stationary,transport and daily food or housing costs.

behind the scenes the application keeps your data organized by saving everything directly to local json fie,meaning your records stay safe even after you close the program. it also features built in input validation to make sure you don't accidentally type incorrect dates,nagative numbers, or invalid categories ,while keeping all its business logic data models ,and helper tools neatly separated into dedicated folders.

## Execution instructions 
1. open terminal inside project directory
2. run command:
 ```bash
  python main.py 
```


