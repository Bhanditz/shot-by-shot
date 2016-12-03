/*jshint esversion: 6 */
import * as d3 from 'd3';

export default function() {
  console.log('working');
  d3.select('#vis').append('p').text('hellooooo');
}
