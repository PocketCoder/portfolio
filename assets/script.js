$.getJSON("meta.json", function(meta) {
    for (i in meta) {
        for (a in meta[i]) {
            const file = `${i}/${meta[i][a]["filename"]}`;
            if (i == "photos") {
                $("#photos .inner").append(`
                <div class="photo" style="background-image: url(${file})">
                    <div class="desc">
                        <h4>${meta[i][a]["name"]}</h4>
                        <h6>${meta[i][a]["year"]}</h6>
                        <p>${meta[i][a]["desc"]}</p>
                        <span>[${meta[i][a]["camera"]} | ${meta[i][a]["film"]}]</span>
                    </div>
                </div>
                `);
            } else if (i == "videos") {
                $("#videos .inner").append(`
                <div class="video">
                    <video id="video" preload playsinline controls>
                        <source src="${file}" type="video/mp4"></source>
                    </video>
                    <div class="video-desc">
                        <h4>${meta[i][a]["name"]}</h4>
                        <h6>${meta[i][a]["year"]}</h6>
                        <p>${meta[i][a]["desc"]}</p>
                    </div>
                </div>
                `);
            } else if (i == "scripts") {
                $("#photos .inner").append(`
                <a href="${file}" target="_blank" class="no-line">
                    <div class="box">
                        <h4>${meta[i][a]["name"]}</h4>
                        <h6>written by ${meta[i][a]["writers"]}.</h6>
                        <span>${meta[i][a]["year"]}</span>
                        <p>&nbsp;</p>
                        <p>${meta[i][a]["desc"]}</p>
                        <br />
                        <p><i>${meta[i][a]["comments"]}</i></p>
                    </div>
                </a>
                `);
            }
        }
    }
});