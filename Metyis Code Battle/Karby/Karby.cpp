/***************************************************************************

    file                 : Karby.cpp
    created              : Wed Apr 6 03:53:44 PM WEST 2022
    copyright            : (C) 2002 TriceraTOP

 ***************************************************************************/

#ifdef _WIN32
#include <windows.h>
#endif

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#include <tgf.h>
#include <track.h>
#include <car.h>
#include <raceman.h>
#include <robottools.h>
#include <robot.h>
#include <bits/stdc++.h>

static tTrack *curTrack;

static void initTrack(int index, tTrack *track, void *carHandle, void **carParmHandle, tSituation *s);
static void newrace(int index, tCarElt *car, tSituation *s);
static void drive(int index, tCarElt *car, tSituation *s);
static void endrace(int index, tCarElt *car, tSituation *s);
static void shutdown(int index);
static int InitFuncPt(int index, void *pt);

using namespace std;

/*
 * Module entry point
 */
extern "C" int Karby(tModInfo *modInfo) {
    memset(modInfo, 0, 10 * sizeof(tModInfo));

    modInfo->name = strdup("Karby"); /* name of the module (short) */
    modInfo->desc = strdup("");      /* description of the module (can be long) */
    modInfo->fctInit = InitFuncPt;   /* init function */
    modInfo->gfId = ROB_IDENT;       /* supported framework version */
    modInfo->index = 1;

    return 0;
}

/* Module interface initialization. */
static int InitFuncPt(int index, void *pt) {
    tRobotItf *itf = (tRobotItf *)pt;

    itf->rbNewTrack = initTrack; /* Give the robot the track view called */
                                 /* for every track change or new race */
    itf->rbNewRace = newrace;    /* Start a new race */
    itf->rbDrive = drive;        /* Drive during race */
    itf->rbPitCmd = NULL;
    itf->rbEndRace = endrace;   /* End of the current race */
    itf->rbShutdown = shutdown; /* Called before the module is unloaded */
    itf->index = index;         /* Index used if multiple interfaces */
    return 0;
}

/* Called for every track change or new race. */
static void initTrack(int index, tTrack *track, void *carHandle, void **carParmHandle, tSituation *s) {
    curTrack = track;
    *carParmHandle = NULL;
}

/* Start a new race. */
static void newrace(int index, tCarElt *car, tSituation *s) {
}

double getAngleDifference(tTrackSeg* seg) {
    return abs(*seg->next->angle - *seg->angle);
}

double getGear(double angle) {
    double a = -1 / (0.5 * PI * PI);
    double b = 6;
    double gear = a * angle * angle + b;

    return (int) gear;
}

double getAcceleration(double angle) {
    double a = -1 / (PI * PI);
    double b = 1;

    return abs(a * angle * angle + b);
}

double getBrake(double angle_difference) {
    return abs(angle_difference) > 0.5? 1 : 0;
}

bool isOnTrack(tCarElt *car) {
    return car->_trkPos.toMiddle <= car->_trkPos.seg->width/3;
}

void returnToTrack(tCarElt *car) {
    float angle = abs(RtTrackSideTgAngleL(&(car->_trkPos)) - car->_yaw);
    bool stuck = abs(angle) > 6.5 || angle + 4.69 > -0.05;
    
        
    car->_steerCmd = abs(remainder(angle, PI) - PI/2) < 0.01 || stuck ? 0 : 0.02;
    car->_gearCmd = stuck ? -1 : 2; 
    car->_accelCmd = 0.3; 
    car->_brakeCmd = 0.0;

    cout << "Angle: " << angle << endl;
    cout << "Steer: " << car->_steerCmd << endl;
}

void driveOnTrack(tCarElt *car) {
    tdble segment_angle = remainder(*car->_trkPos.seg->angle, 2* PI);
    float angle = RtTrackSideTgAngleL(&(car->_trkPos)) - car->_yaw;
    cout << "Angle: " << angle << endl;
    angle = remainder(angle, 2 * PI); // Making sure angle is within -PI and PI
    angle -= car->_trkPos.toMiddle / car->_trkPos.seg->width;

    double angle_difference = getAngleDifference(car->_trkPos.seg);

    car->_steerCmd = angle / car->_steerLock;
    car->_gearCmd = getGear(angle_difference); 
    car->_accelCmd = getAcceleration(angle_difference); 
    car->_brakeCmd = getBrake(angle_difference);
}

/* Drive during race. */
static void drive(int index, tCarElt *car, tSituation *s) {
    memset((void *)&car->ctrl, 0, sizeof(tCarCtrl));

    isOnTrack(car) ? driveOnTrack(car) : returnToTrack(car);

    cout << "Acceleration: " << car->_accelCmd << endl;
}

/* End of the current race */
static void endrace(int index, tCarElt *car, tSituation *s) {
}

/* Called before the module is unloaded */
static void shutdown(int index) {
}
