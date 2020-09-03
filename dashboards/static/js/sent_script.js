function init(){
    const all_seasons_url = 'http://localhost:5000/api/v1.0/text/season'

    fetch(all_seasons_url).then(response => response.json())
        .then(response =>{
            var data = response.results;

            var sorted_data = data.sort((a, b) => b.avg_compound_score - a.avg_compound_score);

            var names = response.results.map(o => o.name);
            var avg_compound_score = response.results.map(o => o.avg_compound_score);


            var ctx = document.getElementById('sent_all_bar').getContext('2d');
            var chart = new Chart(ctx, {
                // The type of chart we want to create
                type: 'horizontalBar',

                // The data for our dataset
                data: {
                    labels: names.slice(0,10),
                    datasets: [{
                        label: 'Average Compound Score',
                        backgroundColor: 'rgb(200, 214, 185)',
                        borderColor: 'rgb(200, 214, 185)',
                        data: avg_compound_score.slice(0,10)
                    }]
                },
            });

        })

    const season_one_url = `http://localhost:5000/api/v1.0/text/season/1`

    fetch(season_one_url).then(response => response.json()).then(response =>{
        var data = response.results;

        var sorted_data = data.sort((a, b) => b.avg_compound_score - a.avg_compound_score);
        
        // var obj_keys = Object.keys(obj.results);
        var names = sorted_data.map(o => o.name);
        var avg_compound_score = sorted_data.map(o => o.avg_compound_score);
        // console.log(nw);

        var ctx = document.getElementById('bar').getContext('2d');
        var chart = new Chart(ctx, {
            // The type of chart we want to create
            type: 'horizontalBar',

            // The data for our dataset
            data: {
                labels: names.slice(0,10),
                datasets: [{
                    label: 'Average Compound Score',
                    backgroundColor: 'rgb(200, 214, 185)',
                    borderColor: 'rgb(200, 214, 185)',
                    data: avg_compound_score.slice(0,10)
                }]
            },
        });
    })

    const word_count_url = `http://localhost:5000/api/v1.0/text/season/all`

    fetch(word_count_url).then(response => response.json()).then(response =>{
        // var obj_keys = Object.keys(obj.results);
        var data = response.results;
        // console.log(data);
        
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
        console.log(sorted_data);
        
        var seasons = sorted_data.map(o => o.season);
        var avg_compound_score = sorted_data.map(o => o.avg_compound_score);

        var ctx = document.getElementById('sent_all_line').getContext('2d');
        var chart = new Chart(ctx, {
            // The type of chart we want to create
            type: 'line',

            // The data for our dataset
            data: {
                labels: seasons,
                datasets: [{
                    label: 'Average Compound Score',
                    // backgroundColor: 'rgb(200, 214, 185)',
                    borderColor: 'rgb(200, 214, 185)',
                    data: avg_compound_score
                }]
            },
        });
    })
}





d3.select('#selDataset1').on('change',optionChanged)

function optionChanged(){
    var dropDownMenu = d3.select('#selDataset1');
    var dataset = dropDownMenu.property('value');    



    var url = `http://localhost:5000/api/v1.0/text/season/${dataset}`

    fetch(url).then(response => response.json()).then(response =>{
        var data = response.results;

        var sorted_data = data.sort((a, b) => b.avg_compound_score - a.avg_compound_score);
        
        // var obj_keys = Object.keys(obj.results);
        var names = sorted_data.map(o => o.name);
        var avg_compound_score = sorted_data.map(o => o.avg_compound_score);
        // console.log(nw);


        var ctx = document.getElementById('bar').getContext('2d');
        var chart = new Chart(ctx, {
            // The type of chart we want to create
            type: 'horizontalBar',

            // The data for our dataset
            data: {
                labels: names.slice(0,10),
                datasets: [{
                    label: 'Total Word Count',
                    backgroundColor: 'rgb(200, 214, 185)',
                    borderColor: 'rgb(200, 214, 185)',
                    data: avg_compound_score.slice(0,10)
                }]
            },
        });
    })
}

    
    init();
