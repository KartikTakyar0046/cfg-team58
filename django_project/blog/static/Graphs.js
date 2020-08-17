var dataset = {dataset};
console.log("----------");
console.log(dataset);

function processData(dataset) {
  var result = [];
  dataset.forEach((item) => result.push(item.fields));
  return result;
}
$.ajax({
  url: $("#pivot-table-container").attr("data-url"),
  dataType: "json",
  success: function (data) {
    new Flexmonster({
      container: "#pivot-table-container",
      componentFolder: "https://cdn.flexmonster.com/",
      width: "100%",
      height: 430,
      toolbar: true,
      report: {
        dataSource: {
          type: "json",
          data: processData(data),
        },
        slice: {},
      },
    });
    new Flexmonster({
      container: "#pivot-chart-container",
      componentFolder: "https://cdn.flexmonster.com/",
      width: "100%",
      height: 430,
      //toolbar: true,
      report: {
        dataSource: {
          type: "json",
          data: processData(data),
        },
        slice: {},
        options: {
          viewType: "charts",
          chart: {
            type: "pie",
          },
        },
      },
    });
  },
});

processData(dataset);