DVM_PERMISSIONS_BY_PERMISSION = {
"BIND_DEVICE_ADMIN" : {
	"Landroid/app/admin/DeviceAdminReceiver;" : [
		("C", "ACTION_DEVICE_ADMIN_ENABLED", "Ljava/lang/String;"),
	],
	"Landroid/app/admin/DevicePolicyManager;" : [
		("F", "getRemoveWarning", "(Landroid/content/ComponentName; Landroid/os/RemoteCallback;)"),
		("F", "reportFailedPasswordAttempt", "()"),
		("F", "reportSuccessfulPasswordAttempt", "()"),
		("F", "setActiveAdmin", "(Landroid/content/ComponentName;)"),
		("F", "setActivePasswordState", "(I I)"),
	],
	"Landroid/app/admin/IDevicePolicyManager$Stub$Proxy;" : [
		("F", "getRemoveWarning", "(Landroid/content/ComponentName; Landroid/os/RemoteCallback;)"),
		("F", "reportFailedPasswordAttempt", "()"),
		("F", "reportSuccessfulPasswordAttempt", "()"),
		("F", "setActiveAdmin", "(Landroid/content/ComponentName;)"),
		("F", "setActivePasswordState", "(I I)"),
	],
},
"READ_SYNC_SETTINGS" : {
	"Landroid/app/ContextImpl$ApplicationContentResolver;" : [
		("F", "getIsSyncable", "(Landroid/accounts/Account; Ljava/lang/String;)"),
		("F", "getMasterSyncAutomatically", "()"),
		("F", "getPeriodicSyncs", "(Landroid/accounts/Account; Ljava/lang/String;)"),
		("F", "getSyncAutomatically", "(Landroid/accounts/Account; Ljava/lang/String;)"),
	],
	"Landroid/content/ContentService;" : [
		("F", "getIsSyncable", "(Landroid/accounts/Account; Ljava/lang/String;)"),
		("F", "getMasterSyncAutomatically", "()"),
		("F", "getPeriodicSyncs", "(Landroid/accounts/Account; Ljava/lang/String;)"),
		("F", "getSyncAutomatically", "(Landroid/accounts/Account; Ljava/lang/String;)"),
	],
	"Landroid/content/ContentResolver;" : [
		("F", "getIsSyncable", "(Landroid/accounts/Account; Ljava/lang/String;)"),
		("F", "getMasterSyncAutomatically", "()"),
		("F", "getPeriodicSyncs", "(Landroid/accounts/Account; Ljava/lang/String;)"),
		("F", "getSyncAutomatically", "(Landroid/accounts/Account; Ljava/lang/String;)"),
	],
	"Landroid/content/IContentService$Stub$Proxy;" : [
		("F", "getIsSyncable", "(Landroid/accounts/Account; Ljava/lang/String;)"),
		("F", "getMasterSyncAutomatically", "()"),
		("F", "getPeriodicSyncs", "(Landroid/accounts/Account; Ljava/lang/String;)"),
		("F", "getSyncAutomatically", "(Landroid/accounts/Account; Ljava/lang/String;)"),
	],
},
"FACTORY_TEST" : {
	"Landroid/content/pm/ApplicationInfo;" : [
		("C", "FLAG_FACTORY_TEST", "I"),
		("C", "flags", "I"),
	],
	"Landroid/content/Intent;" : [
		("C", "IntentResolution", "Ljava/lang/String;"),
		("C", "ACTION_FACTORY_TEST", "Ljava/lang/String;"),
	],
},
"SET_ALWAYS_FINISH" : {
	"Landroid/app/IActivityManager$Stub$Proxy;" : [
		("F", "setAlwaysFinish", "(B)"),
	],
},
"READ_CALENDAR" : {
	"Landroid/provider/Calendar$CalendarAlerts;" : [
		("F", "alarmExists", "(Landroid/content/ContentResolver; J J J)"),
		("F", "findNextAlarmTime", "(Landroid/content/ContentResolver; J)"),
		("F", "query", "(Landroid/content/ContentResolver; [L[Ljava/lang/Strin; Ljava/lang/String; [L[Ljava/lang/Strin; Ljava/lang/String;)"),
	],
	"Landroid/provider/Calendar$Calendars;" : [
		("F", "query", "(Landroid/content/ContentResolver; [L[Ljava/lang/Strin; Ljava/lang/String; Ljava/lang/String;)"),
	],
	"Landroid/provider/Calendar$Events;" : [
		("F", "query", "(Landroid/content/ContentResolver; [L[Ljava/lang/Strin; Ljava/lang/String; Ljava/lang/String;)"),
		("F", "query", "(Landroid/content/ContentResolver; [L[Ljava/lang/Strin;)"),
	],
	"Landroid/provider/Calendar$Instances;" : [
		("F", "query", "(Landroid/content/ContentResolver; [L[Ljava/lang/Strin; J J Ljava/lang/String; Ljava/lang/String;)"),
		("F", "query", "(Landroid/content/ContentResolver; [L[Ljava/lang/Strin; J J)"),
	],
	"Landroid/provider/Calendar$EventDays;" : [
		("F", "query", "(Landroid/content/ContentResolver; I I)"),
	],
},
"ACCESS_DRM" : {
	"Landroid/provider/DrmStore;" : [
		("F", "enforceAccessDrmPermission", "(Landroid/content/Context;)"),
	],
},
"CHANGE_CONFIGURATION" : {
	"Landroid/app/IActivityManager$Stub$Proxy;" : [
		("F", "updateConfiguration", "(Landroid/content/res/Configuration;)"),
	],
},
"SET_ACTIVITY_WATCHER" : {
	"Landroid/app/IActivityManager$Stub$Proxy;" : [
		("F", "profileControl", "(Ljava/lang/String; B Ljava/lang/String; Landroid/os/ParcelFileDescriptor;)"),
		("F", "setActivityController", "(Landroid/app/IActivityController;)"),
	],
},
"GET_PACKAGE_SIZE" : {
	"Landroid/app/ContextImpl$ApplicationPackageManager;" : [
		("F", "getPackageSizeInfo", "(Ljava/lang/String; LIPackageStatsObserver;)"),
		("F", "getPackageSizeInfo", "(Ljava/lang/String; Landroid/content/pm/IPackageStatsObserver;)"),
	],
	"Landroid/content/pm/PackageManager;" : [
		("F", "getPackageSizeInfo", "(Ljava/lang/String; Landroid/content/pm/IPackageStatsObserver;)"),
	],
},
"CONTROL_LOCATION_UPDATES" : {
	"Landroid/telephony/TelephonyManager;" : [
		("F", "disableLocationUpdates", "()"),
		("F", "enableLocationUpdates", "()"),
	],
	"Lcom/android/internal/telephony/ITelephony$Stub$Proxy;" : [
		("F", "disableLocationUpdates", "()"),
		("F", "enableLocationUpdates", "()"),
	],
},
"CLEAR_APP_CACHE" : {
	"Landroid/app/ContextImpl$ApplicationPackageManager;" : [
		("F", "freeStorage", "(J LIntentSender;)"),
		("F", "freeStorageAndNotify", "(J LIPackageDataObserver;)"),
		("F", "freeStorage", "(J Landroid/content/IntentSender;)"),
		("F", "freeStorageAndNotify", "(J Landroid/content/pm/IPackageDataObserver;)"),
	],
	"Landroid/content/pm/PackageManager;" : [
		("F", "freeStorage", "(J Landroid/content/IntentSender;)"),
		("F", "freeStorageAndNotify", "(J Landroid/content/pm/IPackageDataObserver;)"),
	],
	"Landroid/content/pm/IPackageManager$Stub$Proxy;" : [
		("F", "freeStorage", "(J Landroid/content/IntentSender;)"),
		("F", "freeStorageAndNotify", "(J Landroid/content/pm/IPackageDataObserver;)"),
	],
},
"BIND_INPUT_METHOD" : {
	"Landroid/view/inputmethod/InputMethod;" : [
		("C", "SERVICE_INTERFACE", "Ljava/lang/String;"),
	],
},
"SIGNAL_PERSISTENT_PROCESSES" : {
	"Landroid/app/IActivityManager$Stub$Proxy;" : [
		("F", "signalPersistentProcesses", "(I)"),
	],
},
"BATTERY_STATS" : {
	"Lcom/android/internal/app/IBatteryStats$Stub$Proxy;" : [
		("F", "getAwakeTimeBattery", "()"),
		("F", "getAwakeTimePlugged", "()"),
		("F", "getStatistics", "()"),
	],
},
"AUTHENTICATE_ACCOUNTS" : {
	"Landroid/accounts/AccountManager;" : [
		("F", "addAccountExplicitly", "(Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle;)"),
		("F", "getPassword", "(Landroid/accounts/Account;)"),
		("F", "getUserData", "(Landroid/accounts/Account; Ljava/lang/String;)"),
		("F", "peekAuthToken", "(Landroid/accounts/Account; Ljava/lang/String;)"),
		("F", "setAuthToken", "(Landroid/accounts/Account; Ljava/lang/String; Ljava/lang/String;)"),
		("F", "setPassword", "(Landroid/accounts/Account; Ljava/lang/String;)"),
		("F", "setUserData", "(Landroid/accounts/Account; Ljava/lang/String; Ljava/lang/String;)"),
		("F", "addAccountExplicitly", "(Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle;)"),
		("F", "getPassword", "(Landroid/accounts/Account;)"),
		("F", "getUserData", "(Landroid/accounts/Account; Ljava/lang/String;)"),
		("F", "peekAuthToken", "(Landroid/accounts/Account; Ljava/lang/String;)"),
		("F", "setAuthToken", "(Landroid/accounts/Account; Ljava/lang/String; Ljava/lang/String;)"),
		("F", "setPassword", "(Landroid/accounts/Account; Ljava/lang/String;)"),
		("F", "setUserData", "(Landroid/accounts/Account; Ljava/lang/String; Ljava/lang/String;)"),
	],
	"Landroid/accounts/AccountManagerService;" : [
		("F", "addAccount", "(Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle;)"),
		("F", "checkAuthenticateAccountsPermission", "(Landroid/accounts/Account;)"),
		("F", "getPassword", "(Landroid/accounts/Account;)"),
		("F", "getUserData", "(Landroid/accounts/Account; Ljava/lang/String;)"),
		("F", "peekAuthToken", "(Landroid/accounts/Account; Ljava/lang/String;)"),
		("F", "setAuthToken", "(Landroid/accounts/Account; Ljava/lang/String; Ljava/lang/String;)"),
		("F", "setPassword", "(Landroid/accounts/Account; Ljava/lang/String;)"),
		("F", "setUserData", "(Landroid/accounts/Account; Ljava/lang/String; Ljava/lang/String;)"),
	],
	"Landroid/accounts/IAccountManager$Stub$Proxy;" : [
		("F", "addAccount", "(Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle;)"),
		("F", "getPassword", "(Landroid/accounts/Account;)"),
		("F", "getUserData", "(Landroid/accounts/Account; Ljava/lang/String;)"),
		("F", "peekAuthToken", "(Landroid/accounts/Account; Ljava/lang/String;)"),
		("F", "setAuthToken", "(Landroid/accounts/Account; Ljava/lang/String; Ljava/lang/String;)"),
		("F", "setPassword", "(Landroid/accounts/Account; Ljava/lang/String;)"),
		("F", "setUserData", "(Landroid/accounts/Account; Ljava/lang/String; Ljava/lang/String;)"),
	],
},
"CHANGE_BACKGROUND_DATA_SETTING" : {
	"Landroid/net/IConnectivityManager$Stub$Proxy;" : [
		("F", "setBackgroundDataSetting", "(B)"),
	],
	"Landroid/net/ConnectivityManager;" : [
		("F", "setBackgroundDataSetting", "(B)"),
	],
},
"RESTART_PACKAGES" : {
	"Landroid/app/ActivityManagerNative;" : [
		("F", "killBackgroundProcesses", "(Ljava/lang/String;)"),
		("F", "restartPackage", "(Ljava/lang/String;)"),
	],
	"Landroid/app/ActivityManager;" : [
		("F", "killBackgroundProcesses", "(Ljava/lang/String;)"),
		("F", "restartPackage", "(Ljava/lang/String;)"),
	],
},
"CALL_PRIVILEGED" : {
	"Landroid/telephony/TelephonyManager;" : [
		("F", "getCompleteVoiceMailNumber", "()"),
	],
	"Landroid/telephony/PhoneNumberUtils;" : [
		("F", "getNumberFromIntent", "(Landroid/content/Intent; Landroid/content/Context;)"),
	],
},
"SET_WALLPAPER_COMPONENT" : {
	"Landroid/app/IWallpaperManager$Stub$Proxy;" : [
		("F", "setWallpaperComponent", "(Landroid/content/ComponentName;)"),
	],
},
"DISABLE_KEYGUARD" : {
	"Landroid/view/IWindowManager$Stub$Proxy;" : [
		("F", "disableKeyguard", "(Landroid/os/IBinder; Ljava/lang/String;)"),
		("F", "exitKeyguardSecurely", "(Landroid/view/IOnKeyguardExitResult;)"),
		("F", "reenableKeyguard", "(Landroid/os/IBinder;)"),
	],
	"Landroid/app/KeyguardManager;" : [
		("F", "exitKeyguardSecurely", "(Landroid/app/KeyguardManager$OnKeyguardExitResult;)"),
	],
	"Landroid/app/KeyguardManager$KeyguardLock;" : [
		("F", "disableKeyguard", "()"),
		("F", "reenableKeyguard", "()"),
	],
},
"DELETE_PACKAGES" : {
	"Landroid/app/ContextImpl$ApplicationPackageManager;" : [
		("F", "deletePackage", "(Ljava/lang/String; LIPackageDeleteObserver; I)"),
		("F", "deletePackage", "(Ljava/lang/String; LIPackageDeleteObserver; I)"),
	],
	"Landroid/content/pm/PackageManager;" : [
		("F", "deletePackage", "(Ljava/lang/String; LIPackageDeleteObserver; I)"),
	],
	"Landroid/content/pm/IPackageManager$Stub$Proxy;" : [
		("F", "deletePackage", "(Ljava/lang/String; Landroid/content/pm/IPackageDeleteObserver; I)"),
	],
},
"CHANGE_COMPONENT_ENABLED_STATE" : {
	"Landroid/app/ContextImpl$ApplicationPackageManager;" : [
		("F", "setApplicationEnabledSetting", "(Ljava/lang/String; I I)"),
		("F", "setComponentEnabledSetting", "(LComponentName; I I)"),
		("F", "setApplicationEnabledSetting", "(Ljava/lang/String; I I)"),
		("F", "setComponentEnabledSetting", "(Landroid/content/ComponentName; I I)"),
	],
	"Landroid/content/pm/PackageManager;" : [
		("F", "setApplicationEnabledSetting", "(Ljava/lang/String; I I)"),
		("F", "setComponentEnabledSetting", "(Landroid/content/ComponentName; I I)"),
	],
	"Landroid/content/pm/IPackageManager$Stub$Proxy;" : [
		("F", "setApplicationEnabledSetting", "(Ljava/lang/String; I I)"),
		("F", "setComponentEnabledSetting", "(Landroid/content/ComponentName; I I)"),
	],
},
"ASEC_ACCESS" : {
	"Landroid/os/storage/IMountService$Stub$Proxy;" : [
		("F", "getSecureContainerList", "()"),
		("F", "getSecureContainerPath", "(Ljava/lang/String;)"),
		("F", "isSecureContainerMounted", "(Ljava/lang/String;)"),
	],
},
"UPDATE_DEVICE_STATS			" : {
	"Lcom/android/internal/app/IUsageStats$Stub$Proxy;" : [
		("F", "noteLaunchTime", "(LComponentName;)"),
	],
},
"RECORD_AUDIO" : {
	"Landroid/net/sip/SipAudioCall;" : [
		("F", "startAudio", "()"),
	],
	"Landroid/media/MediaRecorder;" : [
		("F", "setAudioSource", "(I)"),
	],
	"Landroid/speech/SpeechRecognizer;" : [
		("F", "cancel", "()"),
		("F", "handleCancelMessage", "()"),
		("F", "handleStartListening", "(Landroid/content/Intent;)"),
		("F", "handleStopMessage", "()"),
		("F", "startListening", "(Landroid/content/Intent;)"),
		("F", "stopListening", "()"),
	],
	"Landroid/media/AudioRecord;" : [
		("F", "<init>", "(I I I I I)"),
	],
},
"ACCESS_MOCK_LOCATION" : {
	"Landroid/location/LocationManager;" : [
		("F", "addTestProvider", "(Ljava/lang/String; B B B B B B B I I)"),
		("F", "clearTestProviderEnabled", "(Ljava/lang/String;)"),
		("F", "clearTestProviderLocation", "(Ljava/lang/String;)"),
		("F", "clearTestProviderStatus", "(Ljava/lang/String;)"),
		("F", "removeTestProvider", "(Ljava/lang/String;)"),
		("F", "setTestProviderEnabled", "(Ljava/lang/String; B)"),
		("F", "setTestProviderLocation", "(Ljava/lang/String; Landroid/location/Location;)"),
		("F", "setTestProviderStatus", "(Ljava/lang/String; I Landroid/os/Bundle; J)"),
		("F", "addTestProvider", "(Ljava/lang/String; B B B B B B B I I)"),
		("F", "clearTestProviderEnabled", "(Ljava/lang/String;)"),
		("F", "clearTestProviderLocation", "(Ljava/lang/String;)"),
		("F", "clearTestProviderStatus", "(Ljava/lang/String;)"),
		("F", "removeTestProvider", "(Ljava/lang/String;)"),
		("F", "setTestProviderEnabled", "(Ljava/lang/String; B)"),
		("F", "setTestProviderLocation", "(Ljava/lang/String; Landroid/location/Location;)"),
		("F", "setTestProviderStatus", "(Ljava/lang/String; I Landroid/os/Bundle; J)"),
	],
	"Landroid/location/ILocationManager$Stub$Proxy;" : [
		("F", "addTestProvider", "(Ljava/lang/String; B B B B B B B I I)"),
		("F", "clearTestProviderEnabled", "(Ljava/lang/String;)"),
		("F", "clearTestProviderLocation", "(Ljava/lang/String;)"),
		("F", "clearTestProviderStatus", "(Ljava/lang/String;)"),
		("F", "removeTestProvider", "(Ljava/lang/String;)"),
		("F", "setTestProviderEnabled", "(Ljava/lang/String; B)"),
		("F", "setTestProviderLocation", "(Ljava/lang/String; Landroid/location/Location;)"),
		("F", "setTestProviderStatus", "(Ljava/lang/String; I Landroid/os/Bundle; J)"),
	],
},
"VIBRATE" : {
	"Landroid/media/AudioManager;" : [
		("C", "EXTRA_RINGER_MODE", "Ljava/lang/String;"),
		("C", "EXTRA_VIBRATE_SETTING", "Ljava/lang/String;"),
		("C", "EXTRA_VIBRATE_TYPE", "Ljava/lang/String;"),
		("C", "FLAG_REMOVE_SOUND_AND_VIBRATE", "I"),
		("C", "FLAG_VIBRATE", "I"),
		("C", "RINGER_MODE_VIBRATE", "I"),
		("C", "VIBRATE_SETTING_CHANGED_ACTION", "Ljava/lang/String;"),
		("C", "VIBRATE_SETTING_OFF", "I"),
		("C", "VIBRATE_SETTING_ON", "I"),
		("C", "VIBRATE_SETTING_ONLY_SILENT", "I"),
		("C", "VIBRATE_TYPE_NOTIFICATION", "I"),
		("C", "VIBRATE_TYPE_RINGER", "I"),
		("F", "getRingerMode", "()"),
		("F", "getVibrateSetting", "(I)"),
		("F", "setRingerMode", "(I)"),
		("F", "setVibrateSetting", "(I I)"),
		("F", "shouldVibrate", "(I)"),
	],
	"Landroid/os/Vibrator;" : [
		("F", "cancel", "()"),
		("F", "vibrate", "([L; I)"),
		("F", "vibrate", "(J)"),
	],
	"Landroid/provider/Settings/System;" : [
		("C", "VIBRATE_ON", "Ljava/lang/String;"),
	],
	"Landroid/app/NotificationManager;" : [
		("F", "notify", "(I Landroid/app/Notification;)"),
		("F", "notify", "(Ljava/lang/String; I Landroid/app/Notification;)"),
	],
	"Landroid/app/Notification/Builder;" : [
		("F", "setDefaults", "(I)"),
	],
	"Landroid/os/IVibratorService$Stub$Proxy;" : [
		("F", "cancelVibrate", "(Landroid/os/IBinder;)"),
		("F", "vibrate", "(J Landroid/os/IBinder;)"),
		("F", "vibratePattern", "([L; I Landroid/os/IBinder;)"),
	],
	"Landroid/app/Notification;" : [
		("C", "DEFAULT_VIBRATE", "I"),
		("C", "defaults", "I"),
	],
},
"ASEC_CREATE" : {
	"Landroid/os/storage/IMountService$Stub$Proxy;" : [
		("F", "createSecureContainer", "(Ljava/lang/String; I Ljava/lang/String; Ljava/lang/String; I)"),
		("F", "finalizeSecureContainer", "(Ljava/lang/String;)"),
	],
},
"WRITE_SECURE_SETTINGS" : {
	"Landroid/bluetooth/BluetoothAdapter;" : [
		("F", "setScanMode", "(I I)"),
		("F", "setScanMode", "(I)"),
	],
	"Landroid/server/BluetoothService;" : [
		("F", "setScanMode", "(I I)"),
	],
	"Landroid/os/IPowerManager$Stub$Proxy;" : [
		("F", "setMaximumScreenOffTimeount", "(I)"),
	],
	"Landroid/content/pm/IPackageManager$Stub$Proxy;" : [
		("F", "setInstallLocation", "(I)"),
	],
	"Landroid/bluetooth/IBluetooth$Stub$Proxy;" : [
		("F", "setScanMode", "(I I)"),
	],
},
"SET_ORIENTATION" : {
	"Landroid/view/IWindowManager$Stub$Proxy;" : [
		("F", "setRotation", "(I B I)"),
	],
},
"PACKAGE_USAGE_STATS" : {
	"Lcom/android/internal/app/IUsageStats$Stub$Proxy;" : [
		("F", "getAllPkgUsageStats", "()"),
		("F", "getPkgUsageStats", "(LComponentName;)"),
	],
},
"FLASHLIGHT" : {
	"Landroid/os/IHardwareService$Stub$Proxy;" : [
		("F", "setFlashlightEnabled", "(B)"),
	],
},
"GLOBAL_SEARCH" : {
	"Landroid/app/SearchManager;" : [
		("C", "EXTRA_SELECT_QUERY", "Ljava/lang/String;"),
		("C", "INTENT_ACTION_GLOBAL_SEARCH", "Ljava/lang/String;"),
	],
	"Landroid/server/search/Searchables;" : [
		("F", "buildSearchableList", "()"),
		("F", "findGlobalSearchActivity", "()"),
	],
},
"CHANGE_WIFI_STATE" : {
	"Landroid/net/wifi/IWifiManager$Stub$Proxy;" : [
		("F", "addOrUpdateNetwork", "(Landroid/net/wifi/WifiConfiguration;)"),
		("F", "disableNetwork", "(I)"),
		("F", "disconnect", "()"),
		("F", "enableNetwork", "(I B)"),
		("F", "pingSupplicant", "()"),
		("F", "reassociate", "()"),
		("F", "reconnect", "()"),
		("F", "removeNetwork", "(I)"),
		("F", "saveConfiguration", "()"),
		("F", "setNumAllowedChannels", "(I B)"),
		("F", "setWifiApEnabled", "(Landroid/net/wifi/WifiConfiguration; B)"),
		("F", "setWifiEnabled", "(B)"),
		("F", "startScan", "(B)"),
	],
	"Landroid/net/wifi/WifiManager;" : [
		("F", "addNetwork", "(Landroid/net/wifi/WifiConfiguration;)"),
		("F", "addOrUpdateNetwork", "(Landroid/net/wifi/WifiConfiguration;)"),
		("F", "disableNetwork", "(I)"),
		("F", "disconnect", "()"),
		("F", "enableNetwork", "(I B)"),
		("F", "pingSupplicant", "()"),
		("F", "reassociate", "()"),
		("F", "reconnect", "()"),
		("F", "removeNetwork", "(I)"),
		("F", "saveConfiguration", "()"),
		("F", "setNumAllowedChannels", "(I B)"),
		("F", "setWifiApEnabled", "(Landroid/net/wifi/WifiConfiguration; B)"),
		("F", "setWifiEnabled", "(B)"),
		("F", "startScan", "()"),
		("F", "startScanActive", "()"),
	],
},
"BROADCAST_STICKY" : {
	"Landroid/app/ExpandableListActivity;" : [
		("F", "removeStickyBroadcast", "(Landroid/content/Intent;)"),
		("F", "sendStickyBroadcast", "(Landroid/content/Intent;)"),
		("F", "sendStickyOrderedBroadcast", "(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"),
	],
	"Landroid/accessibilityservice/AccessibilityService;" : [
		("F", "removeStickyBroadcast", "(Landroid/content/Intent;)"),
		("F", "sendStickyBroadcast", "(Landroid/content/Intent;)"),
		("F", "sendStickyOrderedBroadcast", "(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"),
	],
	"Landroid/accounts/GrantCredentialsPermissionActivity;" : [
		("F", "removeStickyBroadcast", "(Landroid/content/Intent;)"),
		("F", "sendStickyBroadcast", "(Landroid/content/Intent;)"),
		("F", "sendStickyOrderedBroadcast", "(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"),
	],
	"Landroid/app/backup/BackupAgent;" : [
		("F", "removeStickyBroadcast", "(Landroid/content/Intent;)"),
		("F", "sendStickyBroadcast", "(Landroid/content/Intent;)"),
		("F", "sendStickyOrderedBroadcast", "(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"),
	],
	"Landroid/service/wallpaper/WallpaperService;" : [
		("F", "removeStickyBroadcast", "(Landroid/content/Intent;)"),
		("F", "sendStickyBroadcast", "(Landroid/content/Intent;)"),
		("F", "sendStickyOrderedBroadcast", "(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"),
	],
	"Landroid/app/backup/BackupAgentHelper;" : [
		("F", "removeStickyBroadcast", "(Landroid/content/Intent;)"),
		("F", "sendStickyBroadcast", "(Landroid/content/Intent;)"),
		("F", "sendStickyOrderedBroadcast", "(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"),
	],
	"Landroid/accounts/AccountAuthenticatorActivity;" : [
		("F", "removeStickyBroadcast", "(Landroid/content/Intent;)"),
		("F", "sendStickyBroadcast", "(Landroid/content/Intent;)"),
		("F", "sendStickyOrderedBroadcast", "(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"),
	],
	"Landroid/app/IActivityManager$Stub$Proxy;" : [
		("F", "unbroadcastIntent", "(Landroid/app/IApplicationThread; Landroid/content/Intent;)"),
	],
	"Landroid/app/ActivityGroup;" : [
		("F", "removeStickyBroadcast", "(Landroid/content/Intent;)"),
		("F", "sendStickyBroadcast", "(Landroid/content/Intent;)"),
		("F", "sendStickyOrderedBroadcast", "(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"),
	],
	"Landroid/content/ContextWrapper;" : [
		("F", "removeStickyBroadcast", "(Landroid/content/Intent;)"),
		("F", "sendStickyBroadcast", "(Landroid/content/Intent;)"),
		("F", "removeStickyBroadcast", "(Landroid/content/Intent;)"),
		("F", "sendStickyBroadcast", "(Landroid/content/Intent;)"),
		("F", "sendStickyOrderedBroadcast", "(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"),
	],
	"Landroid/app/Activity;" : [
		("F", "removeStickyBroadcast", "(Landroid/content/Intent;)"),
		("F", "sendStickyBroadcast", "(Landroid/content/Intent;)"),
		("F", "sendStickyOrderedBroadcast", "(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"),
	],
	"Landroid/app/ContextImpl;" : [
		("F", "removeStickyBroadcast", "(Landroid/content/Intent;)"),
		("F", "sendStickyBroadcast", "(Landroid/content/Intent;)"),
		("F", "sendStickyOrderedBroadcast", "(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"),
	],
	"Landroid/app/AliasActivity;" : [
		("F", "removeStickyBroadcast", "(Landroid/content/Intent;)"),
		("F", "sendStickyBroadcast", "(Landroid/content/Intent;)"),
		("F", "sendStickyOrderedBroadcast", "(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"),
	],
	"Landroid/content/Context;" : [
		("F", "removeStickyBroadcast", "(Landroid/content/Intent;)"),
		("F", "sendStickyBroadcast", "(Landroid/content/Intent;)"),
		("F", "removeStickyBroadcast", "(Landroid/content/Intent;)"),
		("F", "sendStickyBroadcast", "(Landroid/content/Intent;)"),
		("F", "sendStickyOrderedBroadcast", "(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"),
	],
	"Landroid/service/urlrenderer/UrlRendererService;" : [
		("F", "removeStickyBroadcast", "(Landroid/content/Intent;)"),
		("F", "sendStickyBroadcast", "(Landroid/content/Intent;)"),
		("F", "sendStickyOrderedBroadcast", "(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"),
	],
	"Landroid/app/FullBackupAgent;" : [
		("F", "removeStickyBroadcast", "(Landroid/content/Intent;)"),
		("F", "sendStickyBroadcast", "(Landroid/content/Intent;)"),
		("F", "sendStickyOrderedBroadcast", "(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"),
	],
	"Landroid/app/TabActivity;" : [
		("F", "removeStickyBroadcast", "(Landroid/content/Intent;)"),
		("F", "sendStickyBroadcast", "(Landroid/content/Intent;)"),
		("F", "sendStickyOrderedBroadcast", "(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"),
	],
	"Landroid/view/ContextThemeWrapper;" : [
		("F", "removeStickyBroadcast", "(Landroid/content/Intent;)"),
		("F", "sendStickyBroadcast", "(Landroid/content/Intent;)"),
		("F", "sendStickyOrderedBroadcast", "(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"),
	],
	"Landroid/speech/RecognitionService;" : [
		("F", "removeStickyBroadcast", "(Landroid/content/Intent;)"),
		("F", "sendStickyBroadcast", "(Landroid/content/Intent;)"),
		("F", "sendStickyOrderedBroadcast", "(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"),
	],
	"Landroid/app/IntentService;" : [
		("F", "removeStickyBroadcast", "(Landroid/content/Intent;)"),
		("F", "sendStickyBroadcast", "(Landroid/content/Intent;)"),
		("F", "sendStickyOrderedBroadcast", "(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"),
	],
	"Landroid/inputmethodservice/AbstractInputMethodService;" : [
		("F", "removeStickyBroadcast", "(Landroid/content/Intent;)"),
		("F", "sendStickyBroadcast", "(Landroid/content/Intent;)"),
		("F", "sendStickyOrderedBroadcast", "(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"),
	],
	"Landroid/app/Application;" : [
		("F", "removeStickyBroadcast", "(Landroid/content/Intent;)"),
		("F", "sendStickyBroadcast", "(Landroid/content/Intent;)"),
		("F", "sendStickyOrderedBroadcast", "(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"),
		("F", "sendStickyOrderedBroadcast", "(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"),
	],
	"Landroid/app/ListActivity;" : [
		("F", "removeStickyBroadcast", "(Landroid/content/Intent;)"),
		("F", "sendStickyBroadcast", "(Landroid/content/Intent;)"),
		("F", "sendStickyOrderedBroadcast", "(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"),
	],
	"Landroid/app/Service;" : [
		("F", "removeStickyBroadcast", "(Landroid/content/Intent;)"),
		("F", "sendStickyBroadcast", "(Landroid/content/Intent;)"),
		("F", "sendStickyOrderedBroadcast", "(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"),
	],
	"Landroid/content/MutableContextWrapper;" : [
		("F", "removeStickyBroadcast", "(Landroid/content/Intent;)"),
		("F", "sendStickyBroadcast", "(Landroid/content/Intent;)"),
		("F", "sendStickyOrderedBroadcast", "(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"),
	],
},
"FORCE_STOP_PACKAGES" : {
	"Landroid/app/IActivityManager$Stub$Proxy;" : [
		("F", "forceStopPackage", "(Ljava/lang/String;)"),
	],
	"Landroid/app/ActivityManagerNative;" : [
		("F", "forceStopPackage", "(Ljava/lang/String;)"),
	],
	"Landroid/app/ActivityManager;" : [
		("F", "forceStopPackage", "(Ljava/lang/String;)"),
	],
},
"KILL_BACKGROUND_PROCESSES" : {
	"Landroid/app/IActivityManager$Stub$Proxy;" : [
		("F", "killBackgroundProcesses", "(Ljava/lang/String;)"),
	],
	"Landroid/app/ActivityManager;" : [
		("F", "killBackgroundProcesses", "(Ljava/lang/String;)"),
	],
},
"SET_TIME_ZONE" : {
	"Landroid/app/AlarmManager;" : [
		("F", "setTimeZone", "(Ljava/lang/String;)"),
		("F", "setTimeZone", "(Ljava/lang/String;)"),
	],
	"Landroid/app/IAlarmManager$Stub$Proxy;" : [
		("F", "setTimeZone", "(Ljava/lang/String;)"),
	],
},
"BLUETOOTH_ADMIN" : {
	"Landroid/server/BluetoothA2dpService;" : [
		("F", "connectSink", "(Landroid/bluetooth/BluetoothDevice;)"),
		("F", "disconnectSink", "(Landroid/bluetooth/BluetoothDevice;)"),
		("F", "resumeSink", "(Landroid/bluetooth/BluetoothDevice;)"),
		("F", "setSinkPriority", "(Landroid/bluetooth/BluetoothDevice; I)"),
		("F", "setSinkPriority", "(Landroid/bluetooth/BluetoothDevice; I)"),
		("F", "suspendSink", "(Landroid/bluetooth/BluetoothDevice;)"),
	],
	"Landroid/bluetooth/BluetoothPbap;" : [
		("F", "disconnect", "()"),
	],
	"Landroid/bluetooth/IBluetoothA2dp$Stub$Proxy;" : [
		("F", "connectSink", "(Landroid/bluetooth/BluetoothDevice;)"),
		("F", "disconnectSink", "(Landroid/bluetooth/BluetoothDevice;)"),
		("F", "resumeSink", "(Landroid/bluetooth/BluetoothDevice;)"),
		("F", "setSinkPriority", "(Landroid/bluetooth/BluetoothDevice; I)"),
		("F", "suspendSink", "(Landroid/bluetooth/BluetoothDevice;)"),
	],
	"Landroid/bluetooth/BluetoothAdapter;" : [
		("F", "cancelDiscovery", "()"),
		("F", "disable", "()"),
		("F", "enable", "()"),
		("F", "setName", "(Ljava/lang/String;)"),
		("F", "startDiscovery", "()"),
		("F", "cancelDiscovery", "()"),
		("F", "disable", "()"),
		("F", "enable", "()"),
		("F", "setDiscoverableTimeout", "(I)"),
		("F", "setName", "(Ljava/lang/String;)"),
		("F", "startDiscovery", "()"),
	],
	"Landroid/server/BluetoothService;" : [
		("F", "cancelBondProcess", "(Ljava/lang/String;)"),
		("F", "cancelDiscovery", "()"),
		("F", "cancelPairingUserInput", "(Ljava/lang/String;)"),
		("F", "createBond", "(Ljava/lang/String;)"),
		("F", "disable", "()"),
		("F", "disable", "(B)"),
		("F", "enable", "()"),
		("F", "enable", "(B)"),
		("F", "removeBond", "(Ljava/lang/String;)"),
		("F", "setDiscoverableTimeout", "(I)"),
		("F", "setName", "(Ljava/lang/String;)"),
		("F", "setPairingConfirmation", "(Ljava/lang/String; B)"),
		("F", "setPasskey", "(Ljava/lang/String; I)"),
		("F", "setPin", "(Ljava/lang/String; [L;)"),
		("F", "setTrust", "(Ljava/lang/String; B)"),
		("F", "startDiscovery", "()"),
	],
	"Landroid/bluetooth/BluetoothHeadset;" : [
		("F", "connectHeadset", "(Landroid/bluetooth/BluetoothDevice;)"),
		("F", "disconnectHeadset", "()"),
		("F", "setPriority", "(Landroid/bluetooth/BluetoothDevice; I)"),
	],
	"Landroid/bluetooth/IBluetoothHeadset$Stub$Proxy;" : [
		("F", "connectHeadset", "(Landroid/bluetooth/BluetoothDevice;)"),
		("F", "disconnectHeadset", "()"),
		("F", "setPriority", "(Landroid/bluetooth/BluetoothDevice; I)"),
	],
	"Landroid/bluetooth/BluetoothDevice;" : [
		("F", "cancelBondProcess", "()"),
		("F", "cancelPairingUserInput", "()"),
		("F", "createBond", "()"),
		("F", "removeBond", "()"),
		("F", "setPairingConfirmation", "(B)"),
		("F", "setPasskey", "(I)"),
		("F", "setPin", "([L;)"),
	],
	"Landroid/bluetooth/IBluetoothPbap$Stub$Proxy;" : [
		("F", "connect", "(Landroid/bluetooth/BluetoothDevice;)"),
		("F", "disconnect", "()"),
	],
	"Landroid/bluetooth/BluetoothA2dp;" : [
		("F", "connectSink", "(Landroid/bluetooth/BluetoothDevice;)"),
		("F", "disconnectSink", "(Landroid/bluetooth/BluetoothDevice;)"),
		("F", "resumeSink", "(Landroid/bluetooth/BluetoothDevice;)"),
		("F", "setSinkPriority", "(Landroid/bluetooth/BluetoothDevice; I)"),
		("F", "suspendSink", "(Landroid/bluetooth/BluetoothDevice;)"),
	],
	"Landroid/bluetooth/IBluetooth$Stub$Proxy;" : [
		("F", "cancelBondProcess", "(Ljava/lang/String;)"),
		("F", "cancelDiscovery", "()"),
		("F", "cancelPairingUserInput", "(Ljava/lang/String;)"),
		("F", "createBond", "(Ljava/lang/String;)"),
		("F", "disable", "(B)"),
		("F", "enable", "()"),
		("F", "removeBond", "(Ljava/lang/String;)"),
		("F", "setDiscoverableTimeout", "(I)"),
		("F", "setName", "(Ljava/lang/String;)"),
		("F", "setPairingConfirmation", "(Ljava/lang/String; B)"),
		("F", "setPasskey", "(Ljava/lang/String; I)"),
		("F", "setPin", "(Ljava/lang/String; [L;)"),
		("F", "setTrust", "(Ljava/lang/String; B)"),
		("F", "startDiscovery", "()"),
	]
}
}