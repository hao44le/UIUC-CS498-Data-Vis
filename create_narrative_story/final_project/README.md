# cs498-ddv-final
D3.js visualization for CS498 Data Visualization course final project

# Live Project
This proejct is hosted live on Github Pages at [https://stanleykylee.github.io/cs498-ddv-final](https://stanleykylee.github.io/cs498-ddv-final).

# About the Visualization
This visualization is an interactive slideshow which takes the user through the Dataset of the YouTube trending dataset. The dataset itself contains the YouTube video views across the globe. This visualization focuses on the data from the United States, United Kingdom, Canada, France, India, Japan and Mexico

## Recommended Settings
As the presentation utilize a preset static canvas of 1024x768 pixels, the browsing size of the interactive representation is at least 1280x800 pixels to suit the encompassing content and scene components.

## Templates Scene
The utilization of CSS and FullPage.js takes into account a comprehensive layout for this interactive presentation. Each page is changed
				utilizing a similar technique and content components are kept the equivalent (text dimension and family). Furthermore there is a page transition bar
				on the right side which enables users to skip between various slides. The tooltips which are activated when a user moves their
				mouse over the route modifies the presentation parameters for every navigation menu element.
				
## Annotations
Annotations have been utilized in every one of the three presentation with a comparative procedure of utilizing triggers to change the hidden parameter of
				the explanation. For instance, the Line Chart Visualization has an underlying class of the hidden parameter which controls the showcase
				of the explanations set to false. As a user utilizes the brush bar to trigger changes to the line diagram chart's x-axis
				parameters, it likewise changes this hidden parameter to true. Last but not the least, the comments vanish until the client resets the brush bar
				to zero - hence zooming out back to the default presentation parameters.
		
## Parameters and Triggers
Both parameters and triggers are utilized in the majority of the three presentations. For the Bubble Chart Visualization, parameters for the
				x,y co-ordinates of each bubble are set to an default central location for the All Views Visualization. As a user chooses menu
				things to picked between All Views, Views by Country and Views by Category, it triggers the difference in bubble's x,y co-ordinates
				parameter to their individual groupings.

In Zoomable Sunburst Visualization, each mouse click on a district is a trigger for the way and circular segment parameters. By clicking inside
				an area, you can zoom into the information to investigate the data underneath. Tapping the inside circle will trigger the
				parameters to come back to its qualities one up in the progressive system.
		
For Line Chart Visualization, parameters are set for every Video Category. These parameters are activated to be refreshed as the mouse moves over the presentation, furnishing the client with a preview of the measure of trending videos in a given time. An optional
				parameter and trigger set is the brush bar underneath the line graph. This bar enables the user to zoom into the information to demonstrate a closer
				look of the information. By clicking a set space on the brush bar, it triggers the x-pivot parameter of the line diagram to be refreshed to a
				proportion of the equivalent chose area of the brush bar.

# Reference Materials
## Bubble Chart
+ [stackoverflow question with example code](https://stackoverflow.com/questions/39368919/d3-bubble-chart-bubble-nodes-not-a-function) - [example code snippet](https://jsfiddle.net/r24e8xd7/9/)
+ [Bubble Chart d3 v4 Github Gist by John Alexis Guerra Gomez](https://bl.ocks.org/john-guerra/0d81ccfd24578d5d563c55e785b3b40a)
+ [Animated Bubble Chart by Jim Vallandingham](https://github.com/vlandham/bubble_chart_v4)
+ [d3 API documents on d3-hierarchy - packs](https://github.com/d3/d3-hierarchy/blob/master/README.md#pack)
## Geomapping
+ [Interactive Data Visualization for the Web - Chapter 12. Geomapping by Scott Murray](http://chimera.labs.oreilly.com/books/1230000000345/ch12.html)
+ [Basic US State Map - D3 Github Gist by Michelle Chandra](http://bl.ocks.org/michellechandra/0b2ce4923dc9b5809922)
## Images
+ [https://www.pexels.com/photo/three-men-standing-in-front-of-racing-arcade-machines-929824/](https://www.pexels.com/photo/three-men-standing-in-front-of-racing-arcade-machines-929824/)
+ [https://www.pexels.com/photo/mokup-smartphone-technology-phone-34407/](https://www.pexels.com/photo/mokup-smartphone-technology-phone-34407/)
+ [https://www.pexels.com/photo/photo-of-group-of-people-in-a-meeting-1661004/](https://www.pexels.com/photo/photo-of-group-of-people-in-a-meeting-1661004/)
+ [https://www.pexels.com/photo/amusement-architecture-asia-brick-276114/](https://www.pexels.com/photo/amusement-architecture-asia-brick-276114/)
+ [https://www.pexels.com/photo/wood-texture-background-pine-82256/](https://www.pexels.com/photo/wood-texture-background-pine-82256/)
## Sunburst
+ [https://gist.github.com/mchelen/1481545d38d0304b4d54](https://gist.github.com/mchelen/1481545d38d0304b4d54)
+ [https://gist.github.com/mbostock/4348373](https://gist.github.com/mbostock/4348373)
+ [https://gist.github.com/denjn5/3b74baf5edc4ac93d5e487136481c601](https://gist.github.com/denjn5/3b74baf5edc4ac93d5e487136481c601)
## Line Chart
+ [https://gist.github.com/DStruths/9c042e3a6b66048b5bd4](https://gist.github.com/DStruths/9c042e3a6b66048b5bd4)