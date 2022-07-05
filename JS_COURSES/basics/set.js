const set = new Set([1,2,3]);
set.add(4)
set.add(4)
set.add(4)
// works like python set
set.delete(3)

// set.clear() /// remove all
for(const item of set){
    console.log(item);
}