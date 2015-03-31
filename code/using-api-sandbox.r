# Sandbox for connecting with Yahoo Fantasy Baseball API
library(httr)
library(XML)
library(RJSONIO)
library(ggplot2)
setwd("~/GitHub/fantasy-manager-bot")
keys <- read.csv("~/fantasy-manager-bot-keys.txt", header = F, stringsAsFactors = F)
consumer.key <- keys[1, 1]
consumer.secret <- keys[2, 1]

# See example code online -- http://blog.corynissen.com/2013/12/using-r-to-analyze-yahoo-fantasy.html
# A tutorial on Yahoo's OAuth protocol -- https://nullinfo.wordpress.com/oauth-yahoo/

# Establish connection
  yahoo <- oauth_endpoint("get_request_token", "request_auth", "get_token",
                          base_url = "https://api.login.yahoo.com/oauth/v2")
  myapp <- oauth_app(yahoo, key = consumer.key, secret= consumer.secret)
  token <- oauth1.0_token(yahoo, myapp, cache = FALSE)

# Get information on stuff
  fb.url <- "http://fantasysports.yahooapis.com/fantasy/v2/game/mlb?format=json"
  game.key.json <- GET(fb.url, config(token = token))
  game.key.list <- fromJSON(as.character(game.key.json), asText=T)
  game.key <- game.key.list$fantasy_content$game[[1]]["game_key"]

# Get information on roster
  team.id <- 5
  league.id <- 16550
  team.key <- paste0(game.key, ".l.", league.id, ".t.", team.id)
  #myRosterUrl <- paste0("http://fantasysports.yahooapis.com/fantasy/v2/team/", team.key, "/roster;date=2015-04-06?format=json")
  myRosterUrl <- paste0("http://fantasysports.yahooapis.com/fantasy/v2/team/", team.key, "/roster/players?format=json")
  myGet <- GET(myRosterUrl, config(token = token))  
  response <- fromJSON(as.character(myGet), asText=T)
  
  doc<-htmlParse(myGet)
  root<-xmlRoot(doc)
  xmlSize(root)
  xmlSApply(root, xmlName)
  xmlSApply(root, xmlSize)

# Schedule sample roster switch

# Loop through roster to identify active and inactive players at each position

# Swap players
