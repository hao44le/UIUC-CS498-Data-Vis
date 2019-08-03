# cs498-ddv-final
D3.js visualization for CS498 Data Visualization course final project

# Live Project
This proejct is hosted live on Github Pages at [https://stanleykylee.github.io/cs498-ddv-final](https://stanleykylee.github.io/cs498-ddv-final).

# About the Visualization
This visualization is an interactive slideshow which takes the user through the Dataset of the YouTube trending dataset. The dataset itself contains the YouTube video views across the globe. This visualization focuses on the data from the United States, United Kingdom, Canada, France, India, Japan and Mexico

## Recommended Settings
As the presentation utilize a preset static canvas of 1024x768 pixels, the browsing size of the interactive representation is at least 1280x800 pixels to suit the encompassing content and scene components.

## Templates Scene
The use of CSS and FullPage.js allows for a cohesive template look for the interactive visualization. Each page is transitioned using the same method and text elements are kept the same (font size and family). Additionally there is a page navigation bar on the right side which allows users to skip between different slides. The tooltips which are triggered when a user moves their mouse over the navigation alters the display parameters for each navigation menu item.

## Annotations
Annotations have been used in all three visualizations with a similar process of using triggers to change the hidden paramenter of the annotation. For example, the Line Chart Visualization has an initial state of the hidden parameter which controls the display of the annotations set to false. As a user uses the brush bar to trigger changes to the line chart visualization x-axis parameters, it also changes this hidden parameter to true. In turn the annotations disappear until the user resets the brush bar to zero - thus zooming out back to the default visualization parameters.

## Parameters and Triggers
Both parameters and triggers are used in all of the three visualizations. For the Bubble Chart Visualization, parameters for the x,y co-ordinates of each bubble are set to an initial central position for the All Reviews Visualization. As a user selects menu items to chose between All Reviews, Reviews by State and Reviews by Stars, it triggers the change of bubble’s x,y co-ordinates parameter to their respective groupings.

In Zoomable Sunburst Visualization, each mouse click on a region is a trigger for the path and arc parameters. By clicking within a region, you can zoom into the data to take a look at the information underneath. Clicking the centre circle will trigger the parameters to return to its values one up in the hierarchy.

For Line Chart Visualization, parameters are set for each Restaurant Category. These parameters are triggered to be updated as the mouse moves over the visualization, providing the user with a snapshot of the amount of check-ins in a given time. A secondary parameter and trigger set is the brush bar below the line chart. This bar allows the user to zoom into the data to show a closer look of the data. By clicking a set space on the brush bar, it triggers the x-axis parameter of the line chart to be updated to a ratio of the same selected section of the brush bar.

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