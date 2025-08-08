## Constant Buffers



## Shared Code

Code
[[
#ifndef CONSTANTS_H_
#define CONSTANTS_H_

// --------------------------------------------------------------
// A collection of constants that can be used to tweak the shaders
// To update: run "reloadfx all"
// --------------------------------------------------------------

// --------------------------------------------------------------
// ------------------    Light          -------------------------
// --------------------------------------------------------------


static const float3 LIGHT_DIFFUSE				= float3( 1.0f, 1.0f, 1.0f );
static const float  LIGHT_INTENSITY   			= 1.0f;
static const float  AMBIENT						= 0.2f;
static const float3 MAP_LIGHT_DIFFUSE			= float3( 0.5f, 0.5f, 0.5f );
static const float  MAP_LIGHT_INTENSITY   		= 1.1f;
static const float  MAP_AMBIENT					= 0.85f; // illusionary flat map
static const float	LIGHT_HDR_RANGE 			= 1.0f;

// LIGHT_DIRECTION_X = -1.0						defines.lua   (reload defines)
// LIGHT_DIRECTION_Y = -1.0						defines.lua   (reload defines)
// LIGHT_DIRECTION_Z = 0.5						defines.lua   (reload defines)

// --------------------------------------------------------------
// ------------------    TERRAIN        -------------------------
// --------------------------------------------------------------

static const float 	TERRAIN_TILE_FREQ 			= 128.0f;

// MILD_WINTER_VALUE = ###,						defines.lua   (reload defines)
// NORMAL_WINTER_VALUE = ##,					defines.lua   (reload defines)
// SEVERE_WINTER_VALUE = ###,					defines.lua   (reload defines)


static const float 	BORDER_TILE					= 0.2f;
// BORDER_WIDTH		= ###						defines.lua   (reload defines)



// Snow color									standardfuncsgfx.fxh   
// const static float3 SNOW_COLOR = float3( 0.8f, 0.8f, 0.8f );
// Snow fade									standardfuncsgfx.fxh   
// 	float vSnow = saturate( saturate( vNoise - ( 1.0f - vIsSnow ) ) * 5.0f );

static const float 	TREE_SEASON_MIN 			= 0.5f;
static const float 	TREE_SEASON_FADE_TWEAK 		= 2.5f;


// --------------------------------------------------------------
// ------------------    WATER          -------------------------
// --------------------------------------------------------------


static const float 	WATER_TILE					= 2.25f;
static const float 	WATER_TIME_SCALE			= 5.0f;


// --------------------------------------------------------------
// ------------------    BUILDINGS      -------------------------
// --------------------------------------------------------------

//	PORT_SHIP_OFFSET = 2.0,					defines.lua   (reload defines)
//	SHIP_IN_PORT_SCALE = 0.25,				
//  BUILDING SIZE?



// --------------------------------------------------------------
// ------------------    FOG            -------------------------
// --------------------------------------------------------------

static const float 	FOG_BEGIN					= 80.0f;
static const float 	FOG_END 					= 150.0f;
static const float 	FOG_MAX 					= 0.1f;
static const float3 FOG_COLOR 					= float3( 0.2f, 0.2f, 0.3f );



// --------------------------------------------------------------
// ------------------    BUILDINGS      -------------------------
// --------------------------------------------------------------


static const float  SHADOW_WEIGHT_TERRAIN    	= 0.7f;
static const float  SHADOW_WEIGHT_MAP    		= 0.7f;
static const float  SHADOW_WEIGHT_BORDER   		= 0.7f;
static const float  SHADOW_WEIGHT_WATER   		= 0.5f;
static const float  SHADOW_WEIGHT_RIVER   		= 0.4f;
static const float  SHADOW_WEIGHT_TREE   		= 0.7f;

// LIGHT_SHADOW_DIRECTION_X = -8.0				defines.lua   (reload defines)
// LIGHT_SHADOW_DIRECTION_Y = -8.0				defines.lua   (reload defines)
// LIGHT_SHADOW_DIRECTION_Z = 5.0				defines.lua   (reload defines)


// --------------------------------------------------------------
// ------------------    CAMERA         -------------------------
// --------------------------------------------------------------



// CAMERA_MIN_HEIGHT = 50.0,					defines.lua   (reload defines)
// CAMERA_MAX_HEIGHT = 3000.0,					defines.lua   (reload defines)


// --------------------------------------------------------------
// ------------------    PAPER EFFECT   -------------------------
// --------------------------------------------------------------


static const bool  PAPER						= true;

static const float PAPER_HEIGHT_MIN				= 380.0f;  // no paper effect below this
static const float PAPER_HEIGHT_MAX				= 420.0f;  // full paper effect above this
static const float PAPER_TRANSPARENCY			= 0.3f;  // additional transparency of paper over land
static const float DARKWATER_TRANSPARENCY		= 0.3f;  // additional transparency of paper over land

// static const float LINE1_DISTANCE				= 144.0f;
// static const float LINE1_WIDTH					= 1.0f;
// static const float LINE1_OFFSET					= 0.0f;

// static const float LINE2_DISTANCE				= 48.0f;
// static const float LINE2_WIDTH					= 0.8f;
// static const float LINE2_OFFSET					= 16.0f;

// static const float CREASE_DISTANCE				= 864.0f;
// static const float CREASE_WIDTH					= 6.0f;
// static const float CREASE_OFFSET					= 0.0f;
// static const float CREASE_LIGHT					= 0.0f;
// static const float CREASE_RANDOM_WIDTH			= 0.0f;
// static const float CREASE_RANDOM_LIGHT			= 0.0f;

// --------------------------------------------------------------
// ------------------    FOW            -------------------------
// --------------------------------------------------------------

static const float3	FOW_COLOR 					= float3( 1.0f, 1.0f, 1.0f );
static const float 	FOW_SCALE 					= 512.0f;
static const float 	FOW_TIME_SCALE 				= 0.005f;
static const bool   FOW_FLAT 					= false;
static const float 	FOW_CONTRAST 				= 0.5f;
static const float 	FOW_OPACITY 				= 0.875f;
static const float 	FOW_WEIGHT_BORDER			= 1.0f;
static const float 	FOW_WEIGHT_MAP_NAME			= 0.5f;
#endif //CONSTANTS_H_
]]
