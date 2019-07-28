var height = 200;

var x = d3.scaleLinear().range([200, 0]).domain([5,0]);

var y = d3.scaleLinear().range([height, 0]).domain([0,40]);

var svg = d3.select("svg");

svg.append("g")
   .attr("transform", "translate(" + 50 + "," + 50 + ")")
   .call(d3.axisLeft(y));

svg.append("g")
    .attr("transform",  "translate(" + 50 + "," + 250 + ")")
  .call(d3.axisBottom(x));