# Object Tracker

## Overview

### object_tracker.py

Track objects and assign IDs.

### stabilizer.py (under development)

Stabilize the camera motion for two adjacent frames and transform the first frame toward the second frame.

## Run

```python
from object_tracker import Tracker

...
image_size = (1936, 1216)

tracker = Tracker(image_size, max_patterns=1000000, max_time=1.0)
...

# input prediction data for each frame in order
# input: {'box2d': [x1, y1, x2, y1]}
# output: {'id': id, box2d': [x1, y1, x2, y1], 'mv': [vx, vy], 'scale': [sx, sy], 'occlusion': number_of_occlusions}
prediction = tracker.assign_ids(prediction, image)
...
```

## Test

```bash
python3 object_tracker.py --input /path/to/annotation/directory --output /path/to/output.json

...
"train_00.json" Frame 1: #Car=1, #Pedestrian=15, Time=0.00231242(0.00231242@max), Cost=0.0
"train_00.json" Frame 2: #Car=1, #Pedestrian=17, Time=0.00941324(0.00941324@max), Cost=7.1954494678693175
"train_00.json" Frame 3: #Car=1, #Pedestrian=15, Time=0.01675415(0.01675415@max), Cost=13.910010362372212
...
"train_00.json" Frame 599: #Car=3, #Pedestrian=11, Time=0.01286364(1.03493762@max), Cost=7302.67876091383
"train_00.json" Frame 600: #Car=3, #Pedestrian=12, Time=0.02005100(1.03493762@max), Cost=7311.064619701644
Overall (train_00.json)
    Car: total=2873, sw=196, tp=2476, err=0.06822137
    Pedestrian: total=2868, sw=378, tp=2037, err=0.13179916
    All: err=0.09998258
```
