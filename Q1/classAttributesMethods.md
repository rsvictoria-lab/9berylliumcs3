<img width="820" height="469" alt="Screenshot 2026-09-09 at 12 48 04 AM" src="https://github.com/user-attachments/assets/8d1f9e28-3020-4bb0-8c89-fd54adbe7355" /># Class Attributes and Methods 

## Previous Design

Link to my previous activity: [classObjectUml.md](classObjectUML.md)

## Design Revision

Original class was unchanged 

## Visibility Decisions 

| Attribute | Data Type | Visibility | Why Public/Private? | 

| - Age | Integer | Private | Because age can be used in bad ways |

| + Role | String  | Public | Helpful to know |

| + Name  | String | Public | Helpful to know | 

| - Prescence | Boolean | Private | Can be helpful but house might be robbed when nobody is present |

## Updated UML Class Diagram 
![Class Diagram](![Uploading Screenshot 2026-09-09 at 12.48.04 AM.png…])

## Python Implementation
[View Python Source](Q1/classimplementation.py)



