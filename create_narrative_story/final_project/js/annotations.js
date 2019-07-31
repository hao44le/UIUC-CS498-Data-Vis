// Annotations for Bubble Chart
const bubble_state_annotations = [         
{
    type: d3.annotationLabel,
    note: {
    title: "Majority of Reviews",
    label: "The United Kingdom contains the majority of the YouTube Dataset reviews",
    wrap: 190
    },
    x: 900,
    y: 250,
    dy: -160,
    dx: -120
}]

const bubble_state_makeAnnotations = d3.annotation()
    .type(d3.annotationLabel)
    .annotations(bubble_state_annotations)

const bubble_star_annotations = [
{
    type: d3.annotationLabel,
    note: {
    title: "Most popular Category",
    label: "Regardless of country, the MUSIC contains the majority of the YouTube Dataset reviews",
    wrap: 190
    },
    x: 100,
    y: 350,
    dy: -10,
    dx: -10
}]

const bubble_star_makeAnnotations = d3.annotation()
    .type(d3.annotationLabel)
    .annotations(bubble_star_annotations)

// Annotations for Zoomable Sunburst
const zoom_annotations = [       
{
    type: d3.annotationLabel,
    note: {
    title: "Clustered in NV",
    label: "Top 25 most reviewed is mostly clustered around NV as shown by the outer ring with the same location",
    wrap: 190
    },
    x: 300,
    y: 175,
    dy: -75,
    dx: -120
},
{
    type: d3.annotationLabel,
    note: {
    title: "Top Most Reviewed",
    label: "American (New) restaurant category is the most reviewed restaurant category aggregated across all reviews",
    wrap: 190
    },
    x: 650,
    y: 200,
    dy: -100,
    dx: 200
},
{
    type: d3.annotationLabel,
    note: {
    title: "Aggregated Others",
    label: "Collection of other categories ranked 25 and onwards",
    wrap: 190
    },
    x: 700,
    y: 500,
    dy: 150,
    dx: 200
}]

const zoom_makeAnnotations = d3.annotation()
    .type(d3.annotationLabel)
    .annotations(zoom_annotations)

d3.select("#zoomable_svg")
    .append("g")
    .attr("class", "annotation-group")
    .attr("id", "zoom_annotation")
    .call(zoom_makeAnnotations)

// Annotations for Line Chart
const line_annotations = [
{
    type: d3.annotationLabel,
    note: {
    title: "Weeknight Checkin Spike",
    label: "Spikes nightly for checkins",
    wrap: 190
    },
    x: 250,
    y: 125,
    dy: 0,
    dx: 0
},          
{
    type: d3.annotationLabel,
    note: {
    title: "Weekend Checkin Spike",
    label: "Increased spike of checkins over the weekend",
    wrap: 190
    },
    x: 650,
    y: 200,
    dy: -100,
    dx: -150
}]

const line_makeAnnotations = d3.annotation()
    .type(d3.annotationLabel)
    .annotations(line_annotations)

d3.select("#linechart_svg")
    .append("g")
    .attr("class", "annotation-group")
    .attr("id", "linechart_annotation")
    .call(line_makeAnnotations)