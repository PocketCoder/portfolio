$.getJSON("meta.json", function(meta) {
    for (i in meta) {
        for (a in meta[i]) {
            const img = `${i}/${meta[i][a]["filename"]}`;
            if (i == "photos") {
                $("#photos .inner").append(`
                <div class="photo" style="background-image: url(${img})">
                    <div class="desc">
                        <h4>${meta[i][a]["name"]}</h4>
                        <h6>${meta[i][a]["year"]}</h6>
                        <p>${meta[i][a]["desc"]}</p>
                        <span>[${meta[i][a]["camera"]} | ${meta[i][a]["film"]}]</span>
                    </div>
                </div>
                `);
            } else if (i == "videos") {
                const vid = `${i}/${meta[i][a]["filename"]}`;
                $("#videos .inner").append(`
                <div class="video">
                    <video id="video" preload playsinline controls>
                        <source src="${vid}" type="video/mp4"></source>
                    </video>
                    <div class="video-desc">
                        <h4>${meta[i][a]["name"]}</h4>
                        <h6>${meta[i][a]["year"]}</h6>
                        <p>${meta[i][a]["desc"]}</p>
                    </div>
                </div>
                `);
            } else {
    
            }
        }
    }
});