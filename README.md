# Social-Distancing
This app takes input from a camera or video file and raises an alert whenever social distancing is violated.
The camera client reads the video feed and uses machine learning and image processing to detect the people. 
After that, it calculates the distance between them, and on detecting violation of social distancing, it sends an alert to the other client program, while the 
server facilitates this transaction.

## Requirements
Run 
```
pip install -r requirements 
```
to install the required libraries.

## Usage

To run locally,
in separate terminals,
run

* `python3 server.py`
* `python3 cam_client.py`
* `python3 sec_client.py`
* `python3 social_distancing.py`

To run separately,
go to network.py and change the value of the variable `self.server` to the IP address of the machine hosting the server.
Then go to server.py and change the value of the variable `self.server` to the IP address of the machine hosting the server.
Then follow the steps as above.
