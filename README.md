# song bird classifier

### The story

I recently visited my father and we were both interested by the idea of using his nature cam to build an
end-to-end bird classifier. A few years back I had made an antenna system for him to be able to access
broadband LTE as a home internet solution. Our [first project during this year's visit](https://github.com/mmusil25/handmade-LTE-antenna) 
was to build an LTE antenna out of copper tubing in order to extend the range of the indoor LTE repeater. 

Once the hotspot had a reliable LTE input, we installed two WiFI mesh nodes to broadband the available 5 GHz network
and to use the range extenders as unmanaged switches. These nodes then provided a network access point for both the 
Amcrest camera (IP4M-1053EW) as well as two client terminals. The client terminals were on the some
local network (via the WiFi extenders) which allowed me to access the camera over IP using blue iris. 

I configured Blue Iris to take snapshots of activity centered around the bird feeder in my father's yard. Here is a 
picture of the input frame that was monitored continuously. 

![The entire view field](media/frame.jpg)



### SysML diagrams

![Network diagram](SysML/Dads_network.JPEG)




### Sources

[keras intro](https://keras.io/getting_started/intro_to_keras_for_engineers/)

[the dataset](https://www.kaggle.com/datasets/gpiosenka/100-bird-species)

[how to read in jpg](https://moonbooks.org/Articles/How-to-import-load-an-image-in-python-/#import-an-image-using-matplotlib)

[find a rectangle using opencv](https://www.delftstack.com/howto/python/opencv-detect-rectangle/#:~:text=Use%20the%20findContours%20%28%29%20and%20contourArea%20%28%29%20Function,to%20sort%20different%20rectangles%20according%20to%20their%20area.)

[color sampler - useful for image preprocessing](https://imagecolorpicker.com/)

