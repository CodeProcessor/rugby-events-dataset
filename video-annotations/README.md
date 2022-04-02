# Video Annotations

## Introduction

Video annotations are annotated with the start time and end time of the particular event. 

## Annotation format

| Event Name | start_time | end_time |
| --- | --- | --- |

+ Activity: The name of the activity.

| Event Type | Event Name in Annotations |
| --- | ----------- |
| Scrum | scrum |
| Lineout | lineout |
| Ruck | ruck |

+ start_time: The start time of the activity.
+ end_time: The end time of the activity.


Time can be in two formats:

1. Dot separated format with hours, minutes and seconds.
```text
hh.mm.ss
```
2. Dot separated format withminutes and seconds.
```text
mm.ss
```

## Example format

```text
scrum,37.02,37.17
lineout,39.58,40.01
scrum,40.49,40.56
scrum,48.1,48.23
scrum,49.2,49.28
scrum,55.37,55.54
lineout,56.48,56.52
scrum,57.51,57.56
scrum,1.02.01,1.02.08
lineout,1.06.28,1.06.31
lineout,1.09.05,1.09.07
lineout,1.14.57,1.15.00
lineout,1.16.30,1.16.33
```

## Usage

How to get the starting frame number

ex:
video is 5 fps with following annoatations
```text
lineout,1.14.57,1.15.00
```

Lineout start frame number = (1 * 3600 + 14 * 60 + 57) * 5 = 4497

### No of Annotations

| Event Type | No of Annotations |
| --- | ----- | 
| Scrum | 277 |
| Lineout | 287 |
| Ruck | 363 |

| Total Annotations | 927 |
| --- | ----- |