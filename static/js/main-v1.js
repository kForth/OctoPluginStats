$(window).on('load', function(){
    $(".plugin-chart").each(createInstanceChart);
});

function createInstanceChart(_, elem){
    try{
        var lines = [
            {
                x: $(elem).attr('data-x').split(" "),
                y: $(elem).attr('data-y').split(" "),
                mode: 'lines',
                name: 'instances'
            }
        ];
        var layout = {
            title: 'Active Instances',
            margin: {
                t: 40
            },
            xaxis: {
                linecolor: '#636363',
                linewidth: 3,
                mirror: 'ticks'
            },
            yaxis: {
                linecolor: '#636363',
                linewidth: 3,
                mirror: 'ticks'
            }
        };

        Plotly.newPlot(elem, lines, layout, {displayModeBar: false});
    } catch (e) {
        console.log(elem, e);
    }
}
