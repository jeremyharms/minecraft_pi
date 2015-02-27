#!/usr/bin/python

# Import Minecraft libraries
import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()

# Get player position; used to place the Evereman drop
pPos = mc.player.getTilePos()
pPos.y += 0
pPos.z += 10

block_prim = block.Block(155,0) # white block
block_sec = block.Block(35,15) # black block
block_wood_back = block.Block(24) # sandstone (looks like pine a little bit...)
block_burn_wood = block.Block(17) # darker wood bark
	
def evereman_drop(x,y,z):
	
	# note: place secondary color "background" at z+1
	# place primary color "foreground" at z
	# place wood backing at z+2

	#clear_evereman(x,y,z) #clear him first if he's there
	
	#1: add all black
	mc.setBlocks(x, y, z+1, x+20, y+20, z+1, block_sec)

	#2: add all white
	mc.setBlocks(x, y, z, x+20, y+20, z, block_prim)

	#3: remove large white (with air)
	mc.setBlocks(x+1, y+1, z, x+19, y+19, z, block.AIR)

	#4: add neck
	mc.setBlocks(x+7, y+1, z, x+13, y+2, z, block_prim)

	#5: add mouth
	mc.setBlocks(x+3, y+3, z, x+17, y+5, z, block_prim)

	#6: add mid-face
	mc.setBlocks(x+6, y+6, z, x+14, y+8, z, block_prim)

	#7: add top-face
	mc.setBlocks(x+3, y+9, z, x+17, y+17, z, block_prim)

	#8: remove mouth (air)
	mc.setBlocks(x+4, y+4, z, x+16, y+4, z, block.AIR)

	#9: remove nose (air)
	mc.setBlocks(x+10, y+6, z, x+10, y+10, z, block.AIR)

	#10: remove right eye (air)
	mc.setBlocks(x+4, y+10, z, x+8, y+14, z, block.AIR)

	#11: remove left eye (air)
	mc.setBlocks(x+12, y+10, z, x+16, y+14, z, block.AIR)

	#12: build the back!
	build_back(x,y,z)

	mc.postToChat("Behold... THE EVEREMAN!")
	
def build_back(x,y,z):

	print "build the back!"
	
	# build the wood!
	mc.setBlocks(x, y, z+2, x+20, y+20, z+2, block_wood_back)
	
	# burn in ATL!
	# first, build the four verticals
	mc.setBlocks(x+10, y+1, z+2, x+10, y+4, z+2, block_burn_wood)	
	mc.setBlocks(x+12, y+1, z+2, x+12, y+4, z+2, block_burn_wood)
	mc.setBlocks(x+15, y+1, z+2, x+15, y+4, z+2, block_burn_wood)
	mc.setBlocks(x+18, y+1, z+2, x+18, y+4, z+2, block_burn_wood)
	# now set in the five remaining single blocks
	mc.setBlock(x+11, y+4, z+2, block_burn_wood)
	mc.setBlock(x+14, y+4, z+2, block_burn_wood)
	mc.setBlock(x+16, y+4, z+2, block_burn_wood)
	mc.setBlock(x+11, y+2, z+2, block_burn_wood)
	mc.setBlock(x+19, y+1, z+2, block_burn_wood)

	# burn in 4U!
	# first, build the four verticals
	mc.setBlocks(x+1, y+17, z+2, x+1, y+19, z+2, block_burn_wood)
	mc.setBlocks(x+3, y+16, z+2, x+3, y+19, z+2, block_burn_wood)
	mc.setBlocks(x+5, y+16, z+2, x+5, y+19, z+2, block_burn_wood)
	mc.setBlocks(x+7, y+16, z+2, x+7, y+19, z+2, block_burn_wood)
	# now set in the two remaining single blocks
	mc.setBlock(x+2, y+17, z+2, block_burn_wood)
	mc.setBlock(x+6, y+16, z+2, block_burn_wood)
	

def clear_evereman(x,y,z):
	
	print "clearing evereman..."
	mc.setBlocks(x-10, y, z-15, x+35, y+35, z+15,block.AIR)
	

if __name__ == '__main__':
	print "call evereman_drop()"
	mc.postToChat("Evereman DROP in 3... 2... 1...")
	time.sleep(3)
	evereman_drop(pPos.x, pPos.y, pPos.z)
