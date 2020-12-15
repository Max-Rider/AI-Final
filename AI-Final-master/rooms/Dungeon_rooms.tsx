<?xml version="1.0" encoding="UTF-8"?>
<tileset version="1.4" tiledversion="1.4.2" name="Dungeon_rooms" tilewidth="20" tileheight="22" tilecount="7" columns="0">
 <grid orientation="orthogonal" width="1" height="1"/>
 <tile id="0">
  <image width="20" height="22" source="../tile PNGs/blueWizard.png"/>
 </tile>
 <tile id="1">
  <properties>
   <property name="solid" type="int" value="0"/>
   <property name="stairs" type="int" value="0"/>
  </properties>
  <image width="16" height="16" source="../tile PNGs/floor.png"/>
 </tile>
 <tile id="2">
  <properties>
   <property name="solid" type="int" value="0"/>
   <property name="stairs" type="int" value="1"/>
  </properties>
  <image width="16" height="16" source="../tile PNGs/stairsUp.png"/>
 </tile>
 <tile id="3">
  <properties>
   <property name="solid" type="int" value="1"/>
   <property name="stairs" type="int" value="0"/>
  </properties>
  <image width="16" height="16" source="../tile PNGs/wallSideOne.png"/>
 </tile>
 <tile id="4">
  <properties>
   <property name="solid" type="int" value="1"/>
   <property name="stairs" type="int" value="0"/>
  </properties>
  <image width="16" height="16" source="../tile PNGs/wallSideTwo.png"/>
 </tile>
 <tile id="5">
  <properties>
   <property name="solid" type="int" value="1"/>
   <property name="stairs" type="int" value="0"/>
  </properties>
  <image width="16" height="16" source="../tile PNGs/wallTopOne.png"/>
 </tile>
 <tile id="6">
  <properties>
   <property name="solid" type="int" value="1"/>
   <property name="stairs" type="int" value="0"/>
  </properties>
  <image width="16" height="16" source="../tile PNGs/wallTopTwo.png"/>
 </tile>
</tileset>
