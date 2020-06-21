function init(){
    const all_seasons_url = 'http://localhost:5000/api/v1.0/text/season'

    fetch(all_seasons_url).then(response => response.json())
        .then(response =>{

            var names = response.results.map(o => o.name);
            var total_words = response.results.map(o => o.total_word_count);


            // Sample Values for x axis
            var xValues = names.slice(0,10);

            // OTU IDs for Y axis
            var yValues = total_words.slice(0,10);
            

            // build trace
            var trace1 = {
            x: xValues,
            y: yValues,
            type: 'bar',
            };

            var barData = [trace1];
            
            // plot bar chart
            Plotly.newPlot("all_bar", barData);

        })

    const season_one_url = `http://localhost:5000/api/v1.0/text/season/1`

    fetch(season_one_url).then(response => response.json()).then(response =>{
        // var obj_keys = Object.keys(obj.results);
        var names = response.results.map(o => o.name);
        var total_words = response.results.map(o => o.total_word_count);
        // console.log(nw);


        // Sample Values for x axis
        var xValues = names.slice(0,10);

        // OTU IDs for Y axis
        var yValues = total_words.slice(0,10);
        

        // build trace
        var trace1 = {
        x: xValues,
        y: yValues,
        type: 'bar'
        };

        var barData = [trace1];
        
        // plot bar chart
        Plotly.newPlot("bar", barData);
    })

    const word_count_url = `http://localhost:5000/api/v1.0/text/season/all`

    fetch(word_count_url).then(response => response.json()).then(response =>{
        // var obj_keys = Object.keys(obj.results);
        var data = response.results;
        console.log(data);

        function compare(a, b) {
            // Use toUpperCase() to ignore character casing
            const seasonA = a.season.toUpperCase();
            const seasonB = b.season.toUpperCase();
          
            let comparison = 0;
            if (seasonA > seasonB) {
              comparison = 1;
            } else if (seasonA < seasonB) {
              comparison = -1;
            }
            return comparison;
          }
          
        var sorted_data =  data.sort(compare);

        
        var seasons = sorted_data.map(o => o.season);
        var total_words = sorted_data.map(o => o.total_word_count);

        // Sample Values for x axis
        var xValues = seasons;

        // OTU IDs for Y axis
        var yValues = total_words.slice(0,10);
        

        // build trace
        var trace1 = {
        x: xValues,
        y: yValues,
        type: 'line'
        };

        var barData = [trace1];
        
        // plot bar chart
        Plotly.newPlot("all_line", barData);
    })
}





d3.select('#selDataset1').on('change',optionChanged)

function optionChanged(){
    var dropDownMenu = d3.select('#selDataset1');
    var dataset = dropDownMenu.property('value');    



    var url = `http://localhost:5000/api/v1.0/text/season/${dataset}`

    fetch(url).then(response => response.json()).then(function(obj){
        // var obj_keys = Object.keys(obj.results);
        var names = obj.results.map(o => o.name);
        var total_words = obj.results.map(o => o.total_word_count);
        // console.log(nw);


        // Sample Values for x axis
        var xValues = names.slice(0,10);

        // OTU IDs for Y axis
        var yValues = total_words.slice(0,10);
        

        // build trace
        var trace1 = {
        x: xValues,
        y: yValues,
        type: 'bar'
        };

        var barData = [trace1];
        
        // plot bar chart
        Plotly.newPlot("bar", barData);
    })
}

    
    init();
