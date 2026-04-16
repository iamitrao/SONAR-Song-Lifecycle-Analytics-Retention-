# Spain Top 50 Songs Data Analysis Project
**By: Amit Kumar**

## 1. Introduction
For this project, I wanted to understand how songs perform on the Spotify Spain Top 50 playlist. Unlike the US or UK charts, I noticed that the Spanish market has a lot of Latin music and songs seem to move up and down the charts pretty fast. The goal of this research is to help Atlantic Recording Corporation figure out the best way to release and promote their songs in Spain based on my data analysis.

## 2. How I Analyzed the Data
I used a dataset that tracks the Spain Top 50 songs every day. 
To do this analysis, I wrote a Python script to track the "lifecycle" of each song. This means I found out:
*   When the song first entered the playlist.
*   When it dropped off the playlist.
*   Whether it was a single or part of an album.
*   If the song was marked as "Explicit" or "Clean".

I grouped the songs into different phases, like "New Entry", "Peak Phase" (top 10), and "Decline Phase", so I could see where most songs are at any given time.

## 3. What I Found (Key Results)

Here are the most interesting things I discovered from calculating the KPIs (Key Performance Indicators):

#### A. Songs Need to Get Popular Really Fast, but Don't Last Long
- **Time to Peak:** On average, if a song is going to reach its highest spot, it takes about **9.5 days**. That is super fast!
- **Average Time on Playlist:** A typical song stays on the playlist for about **47.7 days** before falling off. 
- **Survival Rate:** Only **36%** of songs manage to stay on the Top 50 for more than a month (30 days). Most songs drop off really quickly.

#### B. Clean Songs Last Slightly Longer Than Explicit Songs
- I compared how long explicit songs last versus clean songs. Explicit songs get a score of **0.90** when compared to clean songs. This means explicit songs only stay on the charts about 90% as long as clean ones do. So, clean songs might be a little safer for staying popular in the long run.

#### C. Singles Are Way Better Than Album Tracks
- **Single vs Album:** I found that singles stay on the chart **1.5 times longer** than songs that are just tracks released alongside a full album. Releasing singles seems to be the best way to stay on the playlist.

## 4. My Recommendations for Atlantic Records

Based on my analysis, here is what I think Atlantic Records should do:

1. **Spend Marketing Money Early:** Since a song usually peaks in less than 10 days, the marketing team shouldn't wait. Push the song as hard as possible as soon as it comes out.
2. **Release More Singles:** Releasing big albums doesn't work as well in Spain. It's better to release catchy singles one by one because they stay on the charts 50% longer!
3. **Use Clean Versions:** Even though explicit songs are cool and get popular, my data shows clean songs stay on the playlist longer. Releasing clean versions to get on the radio might help songs survive longer.
