// Chart
async function chartIt(url) {
    fetch(url, {
        method: 'get',
    }).then(function (result) {
        console.log(result)
        return result.json()
    }).then(function (data) {

        let canvas = '<canvas id="myChart"></canvas>';
        $('#content').html(canvas);

        const ctx = document.getElementById('myChart');
        const myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: data.labels,
                datasets: [{
                    label: 'Valor',
                    data: data.data,
                    backgroundColor: 'rgba(255, 255, 255, 0.5)',
                    borderColor: 'rbga(255, 99, 132, 1',
                    borderWidth: 1,
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    y: {
                        beginAtZero: true,
                    }
                },
            },
        });
    });
}

window.addEventListener('beforeprint', () => {
    myChart.resize(600, 600);
});
window.addEventListener('afterprint', () => {
    myChart.resize();
});

//  Table
const formatter = new Intl.NumberFormat('pt-BR', {
    style: 'currency',
    currency: 'BRL',
    minimumFractionDigits: 2,
});

async function plot_table(url) {
    let response = await fetch(url)
    let data = await response.json()

    let objSimultaneo = {}
    let arrObj = []

    let i = 0
    while (i < 10) {
        objSimultaneo = { 'Nome': data.labels[i], 'Valor': data.data[i] }
        arrObj.push(objSimultaneo)
        i++
    }

    let table = $('<table class="table">')
    let header = "<tr>"
    for (let k in objSimultaneo) header += "<th>" + k + "</th>"
    header += "</tr>"
    $(header).appendTo(table)


    $.each(arrObj, function (_, value) {
        let row = "<tr>"
        $.each(value, function (key, val) {
            if (key === 'Nome') {
                row += '<td data-title="' + key + '">' + val + "</td>";
            }
            else if (key === 'Valor') {
                row += '<td data-title="' + key + '">' + formatter.format(val) + "</td>";
            }
        });
        row += "</tr>";
        $(table).append(row);
    });
    $('#content').html(table)
}