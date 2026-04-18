
// BAR CHART (ALL RESUMES)

function renderChart(names, scores) {
    const canvas = document.getElementById("chart");

    if (!canvas) {
        console.log("Bar chart canvas not found");
        return;
    }

    new Chart(canvas, {
        type: "bar",
        data: {
            labels: names,
            datasets: [{
                label: "Resume Score",
                data: scores,
                backgroundColor: [
                    "#4CAF50",
                    "#2196F3",
                    "#FF9800",
                    "#F44336",
                    "#9C27B0",
                    "#00BCD4"
                ]
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    display: true
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    max: 100
                }
            }
        }
    });
}



// PIE CHART (PER RESUME)

function renderPieChart(id, matched, missing) {
    const canvas = document.getElementById(id);

    if (!canvas) {
        console.log("Pie chart canvas not found:", id);
        return;
    }

    new Chart(canvas, {
        type: "pie",
        data: {
            labels: ["Matched Skills", "Missing Skills"],
            datasets: [{
                data: [matched, missing],
                backgroundColor: [
                    "#4CAF50",
                    "#F44336"
                ]
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: "bottom"
                }
            }
        }
    });
}
function filterResults() {
    let search = document.getElementById("searchInput").value.toLowerCase();
    let minScore = document.getElementById("minScore").value;

    let cards = document.querySelectorAll(".result-card");

    cards.forEach(card => {
        let name = card.getAttribute("data-name").toLowerCase();
        let score = parseFloat(card.getAttribute("data-score"));

        let matchName = name.includes(search);
        let matchScore = minScore === "" || score >= minScore;

        if (matchName && matchScore) {
            card.style.display = "block";
        } else {
            card.style.display = "none";
        }
    });
}