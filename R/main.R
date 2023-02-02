library(httr,jsonlite)
api <- function(url,query) {
    url <- modify_url(url,query=query)
    resp <- GET(url)
}

strformat = function(str, vals) {
    vars = stringi::stri_match_all(str, regex = "\\{.*?\\}", vectorize_all = FALSE)[[1]][,1]
    x = str
    for (i in seq_along(names(vals))) {
        varName = names(vals)[i]
        varCode = paste0("{", varName, "}")
        x = stringi::stri_replace_all_fixed(x, varCode, vals[[varName]], vectorize_all = TRUE)
    }
    return(x)
}


my_url <- paste0("https://data.arzdigital.com/kline/ohlcv/v1",query=list(base='btc',quote='usdt',resolution='1d',exchange='binance',from=1669753800,to=1670070515000))
resp <- api("https://data.arzdigital.com/kline/ohlcv/v1",query=list(base='btc',quote='usdt',resolution='1d',exchange='binance',from=1669753800,to=1670070515000))
json <- jsonlite::fromJSON(content(resp,"text"),simplifyVector=FALSE)

print(json)
# params <- params()

# my_raw_result <-httr::GET(my_url)

# str(my_raw_result)
# str(my_raw_result$status_code)
# png_file = "{status_code}.png"
# vals = list(status_code=resp$status_code)
# plotpath<- file.path("./R", strformat(png_file,vals))
# png(filename=plotpath)
# plot(resp$status_code,main=file)
# dev.off()
# textplot(my_raw_result$status_code)