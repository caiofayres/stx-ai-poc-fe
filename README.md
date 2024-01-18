# stx-ai-poc-fe

## Base HTML file

base.html file should be put in horizon theme being used, in this case it was at /usr/share/openstack-dashboard/themes/starlingx/templates/

It will be used to add a button at the bottom, and an iframe to the streamlit chat.

## Streamlit Chat

The streamlit chat is a simple python script that uses streamlit to create a chat interface. 

We are using it inside docker and pointing the iframe added in base.html to it.

Our streamlit appication connect's to a HTTP server that is responsible for connecting with OpenAI's API and sending the messages to the chat.

Streamlit is not a simple FE page, but it serve as a proxy to our backend. It is responsible for sending the messages to the HTTP server and receiving the messages from it, instead of connecting the browser directly to the HTTP server.