import React, { useState, useEffect } from 'react'
import * as d3 from 'd3'

import './loss-plot-card.css'

export default function LossPlotCard(props) {
    const requestStatus = props.requestStatus;
    var lineData = props.lineData;
    var data = []

    if (lineData) {
        data = lineData;
    }

    data = data.map((value, valuei) => {
        return [valuei, value]
    })

    // set the dimensions and margins of the graph
    var margin = {top: 10, right: 30, bottom: 30, left: 60},
        width = 460 - margin.left - margin.right,
        height = 400 - margin.top - margin.bottom;

    // append the svg object to the body of the page
    d3.select("#losses").selectAll("*").remove();
    var svg = d3.select("#losses")
    .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
    .append("g")
        .attr("transform",
            "translate(" + margin.left + "," + margin.top + ")");

    // Add X axis --> it is a date format
    var x = d3.scaleLinear()
      .domain([0, d3.max(data, function(d) { return d[0]; })])
      .range([ 0, width ]);
    svg.append("g")
      .call(d3.axisBottom(x));

    // Add Y axis
    var y = d3.scaleLinear()
      .domain([
        d3.min(data, function(d) { return d[1]; }),
        d3.max(data, function(d) { return d[1]; })
      ])
      .range([ height, 0 ]);
    svg.append("g")
      .call(d3.axisLeft(y));
    
    svg.append("path")
        .datum(data)
        .attr("fill", "none")
        .attr("stroke", "steelblue")
        .attr("stroke-width", 2.5)
        .attr("d", d3.line()
            .x(function(d) { return x(d[0]) })
            .y(function(d) { return y(d[1]) })
        )

    return (
        <div className='page-card'>
            <div id="losses"></div>
        </div>
    )
}
