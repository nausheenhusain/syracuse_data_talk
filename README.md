Before class:
=============

1. Read the following news pieces:
	* The Marshall Project, [COVID in prisons](https://www.themarshallproject.org/2020/05/01/a-state-by-state-look-at-coronavirus-in-prisons)
	* South Side Weekly's [ChiVaxBot](https://southsideweekly.com/chivaxbot/) explanation; the bot is [here](https://twitter.com/ChiVaxBot) 

2. Consider the following questions as you're reading:
	* What datasets were needed to write this piece/bulid this bot?
	* What presentation and design decisions were made for each of these projects?
	* As a reader, what appeals to you about the way these datasets are presented? What do you dislike?

3. Read this piece about Karen refugees in [The Daily Orange](http://dailyorange.com/2021/03/karen-refugees-syracuse-rally-justice-recognition/)

4. If you don't have one already, create an account for yourself at [datawrapper.de](https://www.datawrapper.de/) and, if you have time, explore the tools.

5. Make sure Excel works on your machine.

Technical portion of class:
===========================

**If you can follow along on your machine, please do so! If not, it's cool if you want to watch my screen instead.**

1. Go to the [UN data portal](https://rsq.unhcr.org/en/) for refugees.

2. On the left side of the screen, it will give you some options. Choose 'Departures' for View, 2003-2021 for Year, 'Custom selection' then 'Myanmar' for Country of Origin, 'Do not display' for Country of Asylum, and 'Custom selection' then 'All resettlement countries' for Country of Resettlement. Then click 'Show results'. **If you are having issues, go to this link, which has these options chosen for you: https://rsq.unhcr.org/en/#w3SQ.**

3. Click 'Download Data Table CSV'. **If you're having issues, you can also download 'RSQDepartures.csv' from this repository.**

4. Open up the downloaded file in Excel. What aspects of this dataset might we want to think about?

5. Highlight rows 12-188 (just the actual data) and copy-paste it to a new tab. Label that tab 'analysis'.

6. This dataset is a bit confusing because it shows total refugees in each row per country per year. Let's consolidate this with a pivot table!

7. Highlight columns A-H.

8. Click on Insert on your menu bar, and then 'PivotTable'.

9. An option box called 'Create PivotTable' should pop up. For 'Choose where to place the PivotTable' click on 'Existing worksheet' and then click on an empty cell near your data, like J5. Then click 'Okay'.

10. Now we build our data the way we want to see it! Under Field Name, drag 'Year' to the box under 'Rows' because we want our data to be organized by year.

11. In order to see which countries accepted the most refugees, we also want our data to be organized by country. Drag 'Country of Resettlement' under Field Name to the box under 'Columns'.

12. Lastly, let's get our refugee numbers in our data: drag 'Total departures (persons)' under Field Name to the box under 'Values'. Now, we should have a dataset that's slightly easier to understand. **To see the completed pivot table, take a look at 'RSQDepartures_analysis' in this repository.**

13. What we could do from here is just chart these numbers and with some explanatory text, that would be publishable. But, I want us to consider one more aspect of this situation.

14. In our repo, download the file called 'UN_refugees_Admissions.xlsx' and take a look at [the PDF here](https://data2.unhcr.org/en/documents/details/50123). Chris' story mentions that "vast numbers [of the Karen people] remain in refugee camps in Thailand" -- I wanted to see if we could consider this in our numbers too. Luckily, the UN provides (some) data.

***Don't forget that documents are/have data, too!***

15. 'UN_refugees_Admissions.xlsx' shortens our data so that it remains consistent with the data I've compiled from the PDF summaries about refugee camps in Thailand. This is the data we'll chart.

16. Log in to your [datawrapper.de](https://www.datawrapper.de/) account and click on 'New Chart' at the top.

17. Copy the data from 'UN_refugees_Admissions.xlsx' and paste it into the data box in step one. Follow the steps to create a chart for yourself. Remember, your chart should be readable to the average reader!

18. Hit publish. You've published your first chart!

19. Now, let's do this programmatically.
