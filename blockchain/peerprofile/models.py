from django.db import models

# Class to handle the profile of a peer.
# In the SQL dB, we will store the name, designation and photo of each peer in the network.
class PeerProfile(models.Model):
	Name = models.CharField(max_length=250);
	Designation = models.CharField(max_length=250);
	Photo = models.CharField(max_length=1000); #Maybe a link for now. Links can be long so length=1000

# Class to handle the buckets of the peer. There will be two 
# buckets - 
# a) Encash bucket - Will contain coins the peer can encash for himself
# b) Share bucket  - Will contain coins the peer can only use to share with his peers
class PeerBucket(models.Model):
	encash_coins = models.ForeignKey(PeerProfile, on_delete=models.CASCADE) #If peer is deleted from group, so will his bucket.
	# share_coins  = models.ForeignKey(PeerProfile, on_delete=models.CASCADE) #If peer is deleted from group, so will his bucket.


# Class to store a record of all the transactions in a 
# blockchain. This record will be a SQL table which will be independent
# of the dimensions of the network like number of peers in network, etc.
# It might be better to relocate this class to a separate app. Can't decide!! TBD.
class Transactions(models.Model):
	pass