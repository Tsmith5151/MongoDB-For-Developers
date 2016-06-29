for (i=0; i<100, i++){
	for (j=0; j<100; j++){
		x = [];
		for (k=0; k<100; k++)
			{x.push({a:i, b:j,c:k,_id:(100*100*i+100*j+k)})};
		db.example.insert(x)}}
	}
}