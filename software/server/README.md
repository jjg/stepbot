The server provides the following:

*  A websocket server located at a fixed address where robots can connect at start-up to recieve control signals
*  A destination for robot video (and other sensor) feeds
*  A web-based user interface that provides input mechanisms for robot control and renders robot sensor output

## Protocol
Robots attach to the main server websocket and send an initialization message.  The server creates a new websocket for the robot and returns a message that includes the socket port for control signals and potentially a second port to recieve sensor data.  The robot then connects to these new sockets and begins to stream sensor input to the server.  At the same time the robot prepares to receive control signals from the server.

### Control signals


## Server
The server is written in Node.js and uses the Express web framework to provide the content parts of the user interface.  It may also include forms for authenticating users, registering robots, etc.  In addition to the website, the Node.js program uses the websocket library to provide the socket interface(s) used by robots to communicate with the server.


## References

*  Streaming video over websockets: http://phoboslab.org/log/2013/09/html5-live-video-streaming-via-websockets
*  http://www.jperla.com/blog/post/capturing-frames-from-a-webcam-on-linux
