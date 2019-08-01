var width = 1024,
    height = 768,
    radius = (Math.min(width, height) / 2) - 10;
var x = d3.scaleLinear()
    .range([0, 2 * Math.PI]);
var y = d3.scaleSqrt()
    .range([0, radius]);
var zsb_color = d3.scaleOrdinal(d3.schemeCategory20c);
var partition = d3.partition();
var arc = d3.arc()
    .startAngle(function(d) { return Math.max(0, Math.min(2 * Math.PI, x(d.x0))); })
    .endAngle(function(d) { return Math.max(0, Math.min(2 * Math.PI, x(d.x1))); })
    .innerRadius(function(d) { return Math.max(0, y(d.y0)); })
    .outerRadius(function(d) { return Math.max(0, y(d.y1)); });
var zsb_svg = d3.select("#zoomable_sunburst").append("svg")
    .attr('id', 'zoomable_svg')
    .attr("width", width)
    .attr("height", height)
    .append("g")
    .attr("transform", "translate(" + width / 2 + "," + (height / 2) + ")");
var youtube_tree = { "name":"YouTube Database","children":[] };
// tooltip for mouseover functionality
var zsb_tooltip = floatingTooltip('zsb_tooltip', 240);

d3.csv("data/sunburst.csv", function(error, data) {
    if (error) throw error;

    data.forEach(function(d) {
        // iterate through each row of csv data
        var newcat = transverseTree(youtube_tree, d); // is this a new category? lets assume so & then correct

        if (newcat) {
            var youtube_category = {
                "name":d.youtube_category,
                "children": [
                    {"name":"Canada","children":[]},
                    {"name":"Mexico","children":[]},
                    {"name":"United States","children":[]},
                    {"name": "France", "children": []},
                    {"name": "Japan", "children": []},
                    {"name":"United Kingdom","children":[]},
                ]
            };
            youtube_tree.children[youtube_tree.children.length] = youtube_category;
            transverseTree(youtube_tree, d);
        }
    });

    root = d3.hierarchy(youtube_tree)
        .sum(function (d) { return d.reviews; })
        .sort(function(a, b) { return b.value - a.value; });

    root.sum(function(d) { return d.reviews; });
    zsb_svg.selectAll("path")
        .data(partition(root).descendants())
        .enter().append("path")
        .attr("d", arc)
        .style("fill", function(d) { return zsb_color((d.children ? d : d.parent).data.name); })
        .on("click", click)
        .on('mouseover', showZSBDetail)
        .on('mouseout', hideZSBDetail);
});

/*
* Function called on mouseover to display the
* details of a path in the tooltip.
*/
function showZSBDetail(d) {
    var content = '<span class="name">Item: </span><span class="value">' +
                    d.data.name +
                    '</span><br/>' +
                    '<span class="name">Reviews: </span><span class="value">' +
                    d.value +
                    '</span>';

    zsb_tooltip.showTooltip(content, d3.event);
}

/*
* Hides tooltip
*/
function hideZSBDetail(d) {
    zsb_tooltip.hideTooltip();
}

function click(d) {
    d.parent == null ? d3v3.select("#zoom_annotation").classed("hidden", false) : d3v3.select("#zoom_annotation").classed("hidden", true);
    zsb_svg.transition()
        .duration(750)
        .tween("scale", function() {
            var xd = d3.interpolate(x.domain(), [d.x0, d.x1]),
                yd = d3.interpolate(y.domain(), [d.y0, 1]),
                yr = d3.interpolate(y.range(), [d.y0 ? 20 : 0, radius]);
            return function(t) { x.domain(xd(t)); y.domain(yd(t)).range(yr(t)); };
        })
        .selectAll("path")
        .attrTween("d", function(d) { return function() { return arc(d); }; });
}

function transverseTree(tree, d) {
    var newcat = true;
    tree.children.forEach(function(child) {
        if (child.name == d.youtube_category) {
            child.children.forEach(function(grandchild) {
                if(grandchild.name == d.state) {
                    var youtube_video = {"name":d.name,"reviews":d.views};
                    grandchild.children.push(youtube_video);
                    newcat = false; // we matched the category so it's not new
                }
            })
        }
    });
    if (newcat) { return true; } else { return false; }
}

d3.select(self.frameElement).style("height", height + "px");