//Aggregation MongoDB Query Examples (Mongo Shell)

/* Write an aggregation expression to calculate the average population 
of a zip code (postal code) by state. As before, the postal code is in 
the _id field and is considered unique. The collection is assumped to be called "zips" 
and you should name the key in the result set "average_pop" */

//Sum
db.zips.aggregate([
	{'$group':
		{_id:'$state',
		'population':{$sum:'$pop'}
		}
	}
])

//Average
db.zips.aggregate([
	'$group':
		{_id:{
			'state':'$state'
			},
		'population':{$avg:'$pop'}
	}
])


/* You can deduce what your result column names should be from the above output. 
(ignore the issue that a city may have the same name in two different states and is in 
fact two different cities in that case - for eg Springfield, MO and Springfield, MA) */


//Write an aggregation query that will return the postal codes that cover each city.

db.zips.aggregate([
	{'$group':
		{_id:{
			'city':'$city'
			},
		'zip_codes':{$addToSet:'$_id'}
		}
	}
])


/*Write an aggregation query that will return the population of the postal code in each state with 
the highest population. It should return output that looks like this:*/

db.zips.aggregate([
	{'$group':
		{_id:{
			'state':'$state'
			},
		'max_population':{$max:'$pop'}
		}
	}
])
