class Bucket:
    def __init__(self, freq):
        self.prev = None
        self.next = None
        self.freq = freq
        self.keys = set()

class AllOne:

    def __init__(self):
        self.dic = {}
        self.head = Bucket(0)
        self.tail = Bucket(0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def removeNode(self, bucket):
        preBucket = bucket.prev
        nextBucket = bucket.next
        preBucket.next = nextBucket
        nextBucket.pre = preBucket


    def inc(self, key: str) -> None:
        if key in self.dic:
            bucket = self.dic[key]
            freq = bucket.freq
            bucket.keys.remove(key)

            nextBucket = bucket.next
            if nextBucket == self.tail or nextBucket.freq != freq + 1:
                newBucket = Bucket(freq + 1)
                newBucket.keys.add(key)
                newBucket.prev = bucket
                newBucket.next = nextBucket
                nextBucket.prev = newBucket
                bucket.next = newBucket
                self.dic[key] = newBucket
            else:
                nextBucket.keys.add(key)
                self.dic[key] = nextBucket
            
            if not bucket.keys:
                self.removeNode(bucket)
        else:
            firstBucket = self.head.next
            if firstBucket == self.tail or firstBucket.freq > 1:
                newBucket = Bucket(1)
                newBucket.keys.add(key)
                newBucket.prev = self.head
                newBucket.next = firstBucket
                self.head.next = newBucket
                firstBucket.prev = newBucket
                self.dic[key] = newBucket
            else:
                firstBucket.keys.add(key)
                self.dic[key] = firstBucket


    def dec(self, key: str) -> None:
        bucket = self.dic[key]
        freq = bucket.freq
        bucket.keys.remove(key)
        if freq == 1:
            del self.dic[key]
            if not bucket.keys:
                removeNode(bucket)
        if bucket.prev.freq == freq - 1:
            bucket.prev.keys.add(key)
            self.dic[key] = bucket.prev
        else:
            prev_bucket = bucket.prev
            next_bucket = bucket.next
            newBucket = Bucket(freq - 1)
            newBucket.prev = prev_bucket
            prev_bucket.next = newBucket
            newBucket.next = next_bucket
            next_bucket.prev = newBucket
            newBucket.keys.add(key)
            self.dic[key] = newBucket
        
    def getMaxKey(self) -> str:
        max_bucket = self.tail.prev
        if max_bucket == self.head:
            return ""
        return next(iter(max_bucket.keys))

    def getMinKey(self) -> str:
        min_bucket = self.head.next
        if min_bucket == self.tail:
            return ""
        return next(iter(min_bucket.keys))


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()