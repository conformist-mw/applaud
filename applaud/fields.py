# This file is autogenerated by `applaudgen` from `app_store_connect_api.json`.
# Do not modify this file -- YOUR CHANGES WILL BE ERASED!

from .schemas.enums import StringEnum

class AppCategoryField(StringEnum):
    PARENT = 'parent'
    PLATFORMS = 'platforms'
    SUBCATEGORIES = 'subcategories'

class AppClipAdvancedExperienceImageField(StringEnum):
    ASSET_DELIVERY_STATE = 'assetDeliveryState'
    FILE_NAME = 'fileName'
    FILE_SIZE = 'fileSize'
    IMAGE_ASSET = 'imageAsset'
    SOURCE_FILE_CHECKSUM = 'sourceFileChecksum'
    UPLOAD_OPERATIONS = 'uploadOperations'
    UPLOADED = 'uploaded'

class AppClipAdvancedExperienceField(StringEnum):
    ACTION = 'action'
    APP_CLIP = 'appClip'
    BUSINESS_CATEGORY = 'businessCategory'
    DEFAULT_LANGUAGE = 'defaultLanguage'
    HEADER_IMAGE = 'headerImage'
    IS_POWERED_BY = 'isPoweredBy'
    LINK = 'link'
    LOCALIZATIONS = 'localizations'
    PLACE = 'place'
    PLACE_STATUS = 'placeStatus'
    REMOVED = 'removed'
    STATUS = 'status'
    VERSION = 'version'

class AppClipAppStoreReviewDetailField(StringEnum):
    APP_CLIP_DEFAULT_EXPERIENCE = 'appClipDefaultExperience'
    INVOCATION_URLS = 'invocationUrls'

class AppClipDefaultExperienceLocalizationField(StringEnum):
    APP_CLIP_DEFAULT_EXPERIENCE = 'appClipDefaultExperience'
    APP_CLIP_HEADER_IMAGE = 'appClipHeaderImage'
    LOCALE = 'locale'
    SUBTITLE = 'subtitle'

class AppClipHeaderImageField(StringEnum):
    APP_CLIP_DEFAULT_EXPERIENCE_LOCALIZATION = 'appClipDefaultExperienceLocalization'
    ASSET_DELIVERY_STATE = 'assetDeliveryState'
    FILE_NAME = 'fileName'
    FILE_SIZE = 'fileSize'
    IMAGE_ASSET = 'imageAsset'
    SOURCE_FILE_CHECKSUM = 'sourceFileChecksum'
    UPLOAD_OPERATIONS = 'uploadOperations'
    UPLOADED = 'uploaded'

class AppClipDefaultExperienceField(StringEnum):
    ACTION = 'action'
    APP_CLIP = 'appClip'
    APP_CLIP_APP_STORE_REVIEW_DETAIL = 'appClipAppStoreReviewDetail'
    APP_CLIP_DEFAULT_EXPERIENCE_LOCALIZATIONS = 'appClipDefaultExperienceLocalizations'
    APP_CLIP_DEFAULT_EXPERIENCE_TEMPLATE = 'appClipDefaultExperienceTemplate'
    RELEASE_WITH_APP_STORE_VERSION = 'releaseWithAppStoreVersion'

class AppStoreVersionField(StringEnum):
    AGE_RATING_DECLARATION = 'ageRatingDeclaration'
    APP = 'app'
    APP_CLIP_DEFAULT_EXPERIENCE = 'appClipDefaultExperience'
    APP_STORE_REVIEW_DETAIL = 'appStoreReviewDetail'
    APP_STORE_STATE = 'appStoreState'
    APP_STORE_VERSION_LOCALIZATIONS = 'appStoreVersionLocalizations'
    APP_STORE_VERSION_PHASED_RELEASE = 'appStoreVersionPhasedRelease'
    APP_STORE_VERSION_SUBMISSION = 'appStoreVersionSubmission'
    BUILD = 'build'
    COPYRIGHT = 'copyright'
    CREATED_DATE = 'createdDate'
    DOWNLOADABLE = 'downloadable'
    EARLIEST_RELEASE_DATE = 'earliestReleaseDate'
    IDFA_DECLARATION = 'idfaDeclaration'
    PLATFORM = 'platform'
    RELEASE_TYPE = 'releaseType'
    ROUTING_APP_COVERAGE = 'routingAppCoverage'
    USES_IDFA = 'usesIdfa'
    VERSION_STRING = 'versionString'

class AppClipField(StringEnum):
    APP = 'app'
    APP_CLIP_ADVANCED_EXPERIENCES = 'appClipAdvancedExperiences'
    APP_CLIP_DEFAULT_EXPERIENCES = 'appClipDefaultExperiences'
    BUNDLE_ID = 'bundleId'

class AppEncryptionDeclarationField(StringEnum):
    APP = 'app'
    APP_ENCRYPTION_DECLARATION_STATE = 'appEncryptionDeclarationState'
    AVAILABLE_ON_FRENCH_STORE = 'availableOnFrenchStore'
    BUILDS = 'builds'
    CODE_VALUE = 'codeValue'
    CONTAINS_PROPRIETARY_CRYPTOGRAPHY = 'containsProprietaryCryptography'
    CONTAINS_THIRD_PARTY_CRYPTOGRAPHY = 'containsThirdPartyCryptography'
    DOCUMENT_NAME = 'documentName'
    DOCUMENT_TYPE = 'documentType'
    DOCUMENT_URL = 'documentUrl'
    EXEMPT = 'exempt'
    PLATFORM = 'platform'
    UPLOADED_DATE = 'uploadedDate'
    USES_ENCRYPTION = 'usesEncryption'

class AppField(StringEnum):
    APP_CLIPS = 'appClips'
    APP_INFOS = 'appInfos'
    APP_STORE_VERSIONS = 'appStoreVersions'
    AVAILABLE_IN_NEW_TERRITORIES = 'availableInNewTerritories'
    AVAILABLE_TERRITORIES = 'availableTerritories'
    BETA_APP_LOCALIZATIONS = 'betaAppLocalizations'
    BETA_APP_REVIEW_DETAIL = 'betaAppReviewDetail'
    BETA_GROUPS = 'betaGroups'
    BETA_LICENSE_AGREEMENT = 'betaLicenseAgreement'
    BETA_TESTERS = 'betaTesters'
    BUILDS = 'builds'
    BUNDLE_ID = 'bundleId'
    CI_PRODUCT = 'ciProduct'
    CONTENT_RIGHTS_DECLARATION = 'contentRightsDeclaration'
    END_USER_LICENSE_AGREEMENT = 'endUserLicenseAgreement'
    GAME_CENTER_ENABLED_VERSIONS = 'gameCenterEnabledVersions'
    IN_APP_PURCHASES = 'inAppPurchases'
    IS_OR_EVER_WAS_MADE_FOR_KIDS = 'isOrEverWasMadeForKids'
    NAME = 'name'
    PERF_POWER_METRICS = 'perfPowerMetrics'
    PRE_ORDER = 'preOrder'
    PRE_RELEASE_VERSIONS = 'preReleaseVersions'
    PRICES = 'prices'
    PRIMARY_LOCALE = 'primaryLocale'
    SKU = 'sku'

class AppInfoLocalizationField(StringEnum):
    APP_INFO = 'appInfo'
    LOCALE = 'locale'
    NAME = 'name'
    PRIVACY_CHOICES_URL = 'privacyChoicesUrl'
    PRIVACY_POLICY_TEXT = 'privacyPolicyText'
    PRIVACY_POLICY_URL = 'privacyPolicyUrl'
    SUBTITLE = 'subtitle'

class AppInfoField(StringEnum):
    AGE_RATING_DECLARATION = 'ageRatingDeclaration'
    APP = 'app'
    APP_INFO_LOCALIZATIONS = 'appInfoLocalizations'
    APP_STORE_AGE_RATING = 'appStoreAgeRating'
    APP_STORE_STATE = 'appStoreState'
    BRAZIL_AGE_RATING = 'brazilAgeRating'
    KIDS_AGE_BAND = 'kidsAgeBand'
    PRIMARY_CATEGORY = 'primaryCategory'
    PRIMARY_SUBCATEGORY_ONE = 'primarySubcategoryOne'
    PRIMARY_SUBCATEGORY_TWO = 'primarySubcategoryTwo'
    SECONDARY_CATEGORY = 'secondaryCategory'
    SECONDARY_SUBCATEGORY_ONE = 'secondarySubcategoryOne'
    SECONDARY_SUBCATEGORY_TWO = 'secondarySubcategoryTwo'

class AgeRatingDeclarationField(StringEnum):
    ALCOHOL_TOBACCO_OR_DRUG_USE_OR_REFERENCES = 'alcoholTobaccoOrDrugUseOrReferences'
    CONTESTS = 'contests'
    GAMBLING = 'gambling'
    GAMBLING_AND_CONTESTS = 'gamblingAndContests'
    GAMBLING_SIMULATED = 'gamblingSimulated'
    HORROR_OR_FEAR_THEMES = 'horrorOrFearThemes'
    KIDS_AGE_BAND = 'kidsAgeBand'
    MATURE_OR_SUGGESTIVE_THEMES = 'matureOrSuggestiveThemes'
    MEDICAL_OR_TREATMENT_INFORMATION = 'medicalOrTreatmentInformation'
    PROFANITY_OR_CRUDE_HUMOR = 'profanityOrCrudeHumor'
    SEVENTEEN_PLUS = 'seventeenPlus'
    SEXUAL_CONTENT_GRAPHIC_AND_NUDITY = 'sexualContentGraphicAndNudity'
    SEXUAL_CONTENT_OR_NUDITY = 'sexualContentOrNudity'
    UNRESTRICTED_WEB_ACCESS = 'unrestrictedWebAccess'
    VIOLENCE_CARTOON_OR_FANTASY = 'violenceCartoonOrFantasy'
    VIOLENCE_REALISTIC = 'violenceRealistic'
    VIOLENCE_REALISTIC_PROLONGED_GRAPHIC_OR_SADISTIC = 'violenceRealisticProlongedGraphicOrSadistic'

class AppPreOrderField(StringEnum):
    APP = 'app'
    APP_RELEASE_DATE = 'appReleaseDate'
    PRE_ORDER_AVAILABLE_DATE = 'preOrderAvailableDate'

class AppPreviewSetField(StringEnum):
    APP_PREVIEWS = 'appPreviews'
    APP_STORE_VERSION_LOCALIZATION = 'appStoreVersionLocalization'
    PREVIEW_TYPE = 'previewType'

class AppPreviewField(StringEnum):
    APP_PREVIEW_SET = 'appPreviewSet'
    ASSET_DELIVERY_STATE = 'assetDeliveryState'
    FILE_NAME = 'fileName'
    FILE_SIZE = 'fileSize'
    MIME_TYPE = 'mimeType'
    PREVIEW_FRAME_TIME_CODE = 'previewFrameTimeCode'
    PREVIEW_IMAGE = 'previewImage'
    SOURCE_FILE_CHECKSUM = 'sourceFileChecksum'
    UPLOAD_OPERATIONS = 'uploadOperations'
    UPLOADED = 'uploaded'
    VIDEO_URL = 'videoUrl'

class AppPricePointField(StringEnum):
    CUSTOMER_PRICE = 'customerPrice'
    PRICE_TIER = 'priceTier'
    PROCEEDS = 'proceeds'
    TERRITORY = 'territory'

class TerritoryField(StringEnum):
    CURRENCY = 'currency'

class AppPriceTierField(StringEnum):
    PRICE_POINTS = 'pricePoints'

class AppPriceField(StringEnum):
    APP = 'app'
    PRICE_TIER = 'priceTier'

class AppScreenshotSetField(StringEnum):
    APP_SCREENSHOTS = 'appScreenshots'
    APP_STORE_VERSION_LOCALIZATION = 'appStoreVersionLocalization'
    SCREENSHOT_DISPLAY_TYPE = 'screenshotDisplayType'

class AppScreenshotField(StringEnum):
    APP_SCREENSHOT_SET = 'appScreenshotSet'
    ASSET_DELIVERY_STATE = 'assetDeliveryState'
    ASSET_TOKEN = 'assetToken'
    ASSET_TYPE = 'assetType'
    FILE_NAME = 'fileName'
    FILE_SIZE = 'fileSize'
    IMAGE_ASSET = 'imageAsset'
    SOURCE_FILE_CHECKSUM = 'sourceFileChecksum'
    UPLOAD_OPERATIONS = 'uploadOperations'
    UPLOADED = 'uploaded'

class AppStoreReviewAttachmentField(StringEnum):
    APP_STORE_REVIEW_DETAIL = 'appStoreReviewDetail'
    ASSET_DELIVERY_STATE = 'assetDeliveryState'
    FILE_NAME = 'fileName'
    FILE_SIZE = 'fileSize'
    SOURCE_FILE_CHECKSUM = 'sourceFileChecksum'
    UPLOAD_OPERATIONS = 'uploadOperations'
    UPLOADED = 'uploaded'

class AppStoreReviewDetailField(StringEnum):
    APP_STORE_REVIEW_ATTACHMENTS = 'appStoreReviewAttachments'
    APP_STORE_VERSION = 'appStoreVersion'
    CONTACT_EMAIL = 'contactEmail'
    CONTACT_FIRST_NAME = 'contactFirstName'
    CONTACT_LAST_NAME = 'contactLastName'
    CONTACT_PHONE = 'contactPhone'
    DEMO_ACCOUNT_NAME = 'demoAccountName'
    DEMO_ACCOUNT_PASSWORD = 'demoAccountPassword'
    DEMO_ACCOUNT_REQUIRED = 'demoAccountRequired'
    NOTES = 'notes'

class AppStoreVersionLocalizationField(StringEnum):
    APP_PREVIEW_SETS = 'appPreviewSets'
    APP_SCREENSHOT_SETS = 'appScreenshotSets'
    APP_STORE_VERSION = 'appStoreVersion'
    DESCRIPTION = 'description'
    KEYWORDS = 'keywords'
    LOCALE = 'locale'
    MARKETING_URL = 'marketingUrl'
    PROMOTIONAL_TEXT = 'promotionalText'
    SUPPORT_URL = 'supportUrl'
    WHATS_NEW = 'whatsNew'

class AppStoreVersionSubmissionField(StringEnum):
    APP_STORE_VERSION = 'appStoreVersion'

class IdfaDeclarationField(StringEnum):
    APP_STORE_VERSION = 'appStoreVersion'
    ATTRIBUTES_ACTION_WITH_PREVIOUS_AD = 'attributesActionWithPreviousAd'
    ATTRIBUTES_APP_INSTALLATION_TO_PREVIOUS_AD = 'attributesAppInstallationToPreviousAd'
    HONORS_LIMITED_AD_TRACKING = 'honorsLimitedAdTracking'
    SERVES_ADS = 'servesAds'

class RoutingAppCoverageField(StringEnum):
    APP_STORE_VERSION = 'appStoreVersion'
    ASSET_DELIVERY_STATE = 'assetDeliveryState'
    FILE_NAME = 'fileName'
    FILE_SIZE = 'fileSize'
    SOURCE_FILE_CHECKSUM = 'sourceFileChecksum'
    UPLOAD_OPERATIONS = 'uploadOperations'
    UPLOADED = 'uploaded'

class AppStoreVersionPhasedReleaseField(StringEnum):
    APP_STORE_VERSION = 'appStoreVersion'
    CURRENT_DAY_NUMBER = 'currentDayNumber'
    PHASED_RELEASE_STATE = 'phasedReleaseState'
    START_DATE = 'startDate'
    TOTAL_PAUSE_DURATION = 'totalPauseDuration'

class BuildField(StringEnum):
    APP = 'app'
    APP_ENCRYPTION_DECLARATION = 'appEncryptionDeclaration'
    APP_STORE_VERSION = 'appStoreVersion'
    BETA_APP_REVIEW_SUBMISSION = 'betaAppReviewSubmission'
    BETA_BUILD_LOCALIZATIONS = 'betaBuildLocalizations'
    BETA_GROUPS = 'betaGroups'
    BUILD_AUDIENCE_TYPE = 'buildAudienceType'
    BUILD_BETA_DETAIL = 'buildBetaDetail'
    BUILD_BUNDLES = 'buildBundles'
    COMPUTED_MIN_MAC_OS_VERSION = 'computedMinMacOsVersion'
    DIAGNOSTIC_SIGNATURES = 'diagnosticSignatures'
    EXPIRATION_DATE = 'expirationDate'
    EXPIRED = 'expired'
    ICON_ASSET_TOKEN = 'iconAssetToken'
    ICONS = 'icons'
    INDIVIDUAL_TESTERS = 'individualTesters'
    LS_MINIMUM_SYSTEM_VERSION = 'lsMinimumSystemVersion'
    MIN_OS_VERSION = 'minOsVersion'
    PERF_POWER_METRICS = 'perfPowerMetrics'
    PRE_RELEASE_VERSION = 'preReleaseVersion'
    PROCESSING_STATE = 'processingState'
    UPLOADED_DATE = 'uploadedDate'
    USES_NON_EXEMPT_ENCRYPTION = 'usesNonExemptEncryption'
    VERSION = 'version'

class BetaLicenseAgreementField(StringEnum):
    AGREEMENT_TEXT = 'agreementText'
    APP = 'app'

class BetaAppReviewDetailField(StringEnum):
    APP = 'app'
    CONTACT_EMAIL = 'contactEmail'
    CONTACT_FIRST_NAME = 'contactFirstName'
    CONTACT_LAST_NAME = 'contactLastName'
    CONTACT_PHONE = 'contactPhone'
    DEMO_ACCOUNT_NAME = 'demoAccountName'
    DEMO_ACCOUNT_PASSWORD = 'demoAccountPassword'
    DEMO_ACCOUNT_REQUIRED = 'demoAccountRequired'
    NOTES = 'notes'

class BetaAppLocalizationField(StringEnum):
    APP = 'app'
    DESCRIPTION = 'description'
    FEEDBACK_EMAIL = 'feedbackEmail'
    LOCALE = 'locale'
    MARKETING_URL = 'marketingUrl'
    PRIVACY_POLICY_URL = 'privacyPolicyUrl'
    TV_OS_PRIVACY_POLICY = 'tvOsPrivacyPolicy'

class InAppPurchaseField(StringEnum):
    APPS = 'apps'
    IN_APP_PURCHASE_TYPE = 'inAppPurchaseType'
    PRODUCT_ID = 'productId'
    REFERENCE_NAME = 'referenceName'
    STATE = 'state'

class PreReleaseVersionField(StringEnum):
    APP = 'app'
    BUILDS = 'builds'
    PLATFORM = 'platform'
    VERSION = 'version'

class CiProductField(StringEnum):
    ADDITIONAL_REPOSITORIES = 'additionalRepositories'
    APP = 'app'
    BUILD_RUNS = 'buildRuns'
    BUNDLE_ID = 'bundleId'
    CREATED_DATE = 'createdDate'
    NAME = 'name'
    PRIMARY_REPOSITORIES = 'primaryRepositories'
    PRODUCT_TYPE = 'productType'
    WORKFLOWS = 'workflows'

class BetaGroupField(StringEnum):
    APP = 'app'
    BETA_TESTERS = 'betaTesters'
    BUILDS = 'builds'
    CREATED_DATE = 'createdDate'
    FEEDBACK_ENABLED = 'feedbackEnabled'
    HAS_ACCESS_TO_ALL_BUILDS = 'hasAccessToAllBuilds'
    IOS_BUILDS_AVAILABLE_FOR_APPLE_SILICON_MAC = 'iosBuildsAvailableForAppleSiliconMac'
    IS_INTERNAL_GROUP = 'isInternalGroup'
    NAME = 'name'
    PUBLIC_LINK = 'publicLink'
    PUBLIC_LINK_ENABLED = 'publicLinkEnabled'
    PUBLIC_LINK_ID = 'publicLinkId'
    PUBLIC_LINK_LIMIT = 'publicLinkLimit'
    PUBLIC_LINK_LIMIT_ENABLED = 'publicLinkLimitEnabled'

class GameCenterEnabledVersionField(StringEnum):
    APP = 'app'
    COMPATIBLE_VERSIONS = 'compatibleVersions'
    ICON_ASSET = 'iconAsset'
    PLATFORM = 'platform'
    VERSION_STRING = 'versionString'

class EndUserLicenseAgreementField(StringEnum):
    AGREEMENT_TEXT = 'agreementText'
    APP = 'app'
    TERRITORIES = 'territories'

class PerfPowerMetricField(StringEnum):
    DEVICE_TYPE = 'deviceType'
    METRIC_TYPE = 'metricType'
    PLATFORM = 'platform'

class BetaAppClipInvocationField(StringEnum):
    BETA_APP_CLIP_INVOCATION_LOCALIZATIONS = 'betaAppClipInvocationLocalizations'
    BUILD_BUNDLE = 'buildBundle'
    URL = 'url'

class BetaAppReviewSubmissionField(StringEnum):
    BETA_REVIEW_STATE = 'betaReviewState'
    BUILD = 'build'
    SUBMITTED_DATE = 'submittedDate'

class BetaBuildLocalizationField(StringEnum):
    BUILD = 'build'
    LOCALE = 'locale'
    WHATS_NEW = 'whatsNew'

class BetaTesterField(StringEnum):
    APPS = 'apps'
    BETA_GROUPS = 'betaGroups'
    BUILDS = 'builds'
    EMAIL = 'email'
    FIRST_NAME = 'firstName'
    INVITE_TYPE = 'inviteType'
    LAST_NAME = 'lastName'

class BuildBetaDetailField(StringEnum):
    AUTO_NOTIFY_ENABLED = 'autoNotifyEnabled'
    BUILD = 'build'
    EXTERNAL_BUILD_STATE = 'externalBuildState'
    INTERNAL_BUILD_STATE = 'internalBuildState'

class DiagnosticSignatureField(StringEnum):
    DIAGNOSTIC_TYPE = 'diagnosticType'
    LOGS = 'logs'
    SIGNATURE = 'signature'
    WEIGHT = 'weight'

class BuildIconField(StringEnum):
    ICON_ASSET = 'iconAsset'
    ICON_TYPE = 'iconType'

class BundleIdField(StringEnum):
    APP = 'app'
    BUNDLE_ID_CAPABILITIES = 'bundleIdCapabilities'
    IDENTIFIER = 'identifier'
    NAME = 'name'
    PLATFORM = 'platform'
    PROFILES = 'profiles'
    SEED_ID = 'seedId'

class BundleIdCapabilityField(StringEnum):
    BUNDLE_ID = 'bundleId'
    CAPABILITY_TYPE = 'capabilityType'
    SETTINGS = 'settings'

class ProfileField(StringEnum):
    BUNDLE_ID = 'bundleId'
    CERTIFICATES = 'certificates'
    CREATED_DATE = 'createdDate'
    DEVICES = 'devices'
    EXPIRATION_DATE = 'expirationDate'
    NAME = 'name'
    PLATFORM = 'platform'
    PROFILE_CONTENT = 'profileContent'
    PROFILE_STATE = 'profileState'
    PROFILE_TYPE = 'profileType'
    UUID = 'uuid'

class CertificateField(StringEnum):
    CERTIFICATE_CONTENT = 'certificateContent'
    CERTIFICATE_TYPE = 'certificateType'
    CSR_CONTENT = 'csrContent'
    DISPLAY_NAME = 'displayName'
    EXPIRATION_DATE = 'expirationDate'
    NAME = 'name'
    PLATFORM = 'platform'
    SERIAL_NUMBER = 'serialNumber'

class CiArtifactField(StringEnum):
    DOWNLOAD_URL = 'downloadUrl'
    FILE_NAME = 'fileName'
    FILE_SIZE = 'fileSize'
    FILE_TYPE = 'fileType'

class CiBuildActionField(StringEnum):
    ACTION_TYPE = 'actionType'
    ARTIFACTS = 'artifacts'
    BUILD_RUN = 'buildRun'
    COMPLETION_STATUS = 'completionStatus'
    EXECUTION_PROGRESS = 'executionProgress'
    FINISHED_DATE = 'finishedDate'
    IS_REQUIRED_TO_PASS = 'isRequiredToPass'
    ISSUE_COUNTS = 'issueCounts'
    ISSUES = 'issues'
    NAME = 'name'
    STARTED_DATE = 'startedDate'
    TEST_RESULTS = 'testResults'

class CiIssueField(StringEnum):
    CATEGORY = 'category'
    FILE_SOURCE = 'fileSource'
    ISSUE_TYPE = 'issueType'
    MESSAGE = 'message'

class CiBuildRunField(StringEnum):
    ACTIONS = 'actions'
    BUILD_RUN = 'buildRun'
    BUILDS = 'builds'
    CANCEL_REASON = 'cancelReason'
    CLEAN = 'clean'
    COMPLETION_STATUS = 'completionStatus'
    CREATED_DATE = 'createdDate'
    DESTINATION_BRANCH = 'destinationBranch'
    DESTINATION_COMMIT = 'destinationCommit'
    EXECUTION_PROGRESS = 'executionProgress'
    FINISHED_DATE = 'finishedDate'
    IS_PULL_REQUEST_BUILD = 'isPullRequestBuild'
    ISSUE_COUNTS = 'issueCounts'
    NUMBER = 'number'
    PRODUCT = 'product'
    PULL_REQUEST = 'pullRequest'
    SOURCE_BRANCH_OR_TAG = 'sourceBranchOrTag'
    SOURCE_COMMIT = 'sourceCommit'
    START_REASON = 'startReason'
    STARTED_DATE = 'startedDate'
    WORKFLOW = 'workflow'

class CiTestResultField(StringEnum):
    CLASS_NAME = 'className'
    DESTINATION_TEST_RESULTS = 'destinationTestResults'
    FILE_SOURCE = 'fileSource'
    MESSAGE = 'message'
    NAME = 'name'
    STATUS = 'status'

class CiMacOsVersionField(StringEnum):
    NAME = 'name'
    VERSION = 'version'
    XCODE_VERSIONS = 'xcodeVersions'

class CiXcodeVersionField(StringEnum):
    MAC_OS_VERSIONS = 'macOsVersions'
    NAME = 'name'
    TEST_DESTINATIONS = 'testDestinations'
    VERSION = 'version'

class CiWorkflowField(StringEnum):
    ACTIONS = 'actions'
    BRANCH_START_CONDITION = 'branchStartCondition'
    BUILD_RUNS = 'buildRuns'
    CLEAN = 'clean'
    CONTAINER_FILE_PATH = 'containerFilePath'
    DESCRIPTION = 'description'
    IS_ENABLED = 'isEnabled'
    IS_LOCKED_FOR_EDITING = 'isLockedForEditing'
    LAST_MODIFIED_DATE = 'lastModifiedDate'
    MAC_OS_VERSION = 'macOsVersion'
    NAME = 'name'
    PRODUCT = 'product'
    PULL_REQUEST_START_CONDITION = 'pullRequestStartCondition'
    REPOSITORY = 'repository'
    SCHEDULED_START_CONDITION = 'scheduledStartCondition'
    TAG_START_CONDITION = 'tagStartCondition'
    XCODE_VERSION = 'xcodeVersion'

class ScmRepositoryField(StringEnum):
    DEFAULT_BRANCH = 'defaultBranch'
    GIT_REFERENCES = 'gitReferences'
    HTTP_CLONE_URL = 'httpCloneUrl'
    LAST_ACCESSED_DATE = 'lastAccessedDate'
    OWNER_NAME = 'ownerName'
    PULL_REQUESTS = 'pullRequests'
    REPOSITORY_NAME = 'repositoryName'
    SCM_PROVIDER = 'scmProvider'
    SSH_CLONE_URL = 'sshCloneUrl'

class DeviceField(StringEnum):
    ADDED_DATE = 'addedDate'
    DEVICE_CLASS = 'deviceClass'
    MODEL = 'model'
    NAME = 'name'
    PLATFORM = 'platform'
    STATUS = 'status'
    UDID = 'udid'

class ScmGitReferenceField(StringEnum):
    CANONICAL_NAME = 'canonicalName'
    IS_DELETED = 'isDeleted'
    KIND = 'kind'
    NAME = 'name'
    REPOSITORY = 'repository'

class ScmProviderField(StringEnum):
    REPOSITORIES = 'repositories'
    SCM_PROVIDER_TYPE = 'scmProviderType'
    URL = 'url'

class ScmPullRequestField(StringEnum):
    DESTINATION_BRANCH_NAME = 'destinationBranchName'
    DESTINATION_REPOSITORY_NAME = 'destinationRepositoryName'
    DESTINATION_REPOSITORY_OWNER = 'destinationRepositoryOwner'
    IS_CLOSED = 'isClosed'
    IS_CROSS_REPOSITORY = 'isCrossRepository'
    NUMBER = 'number'
    REPOSITORY = 'repository'
    SOURCE_BRANCH_NAME = 'sourceBranchName'
    SOURCE_REPOSITORY_NAME = 'sourceRepositoryName'
    SOURCE_REPOSITORY_OWNER = 'sourceRepositoryOwner'
    TITLE = 'title'
    WEB_URL = 'webUrl'

class UserInvitationField(StringEnum):
    ALL_APPS_VISIBLE = 'allAppsVisible'
    EMAIL = 'email'
    EXPIRATION_DATE = 'expirationDate'
    FIRST_NAME = 'firstName'
    LAST_NAME = 'lastName'
    PROVISIONING_ALLOWED = 'provisioningAllowed'
    ROLES = 'roles'
    VISIBLE_APPS = 'visibleApps'

class UserField(StringEnum):
    ALL_APPS_VISIBLE = 'allAppsVisible'
    FIRST_NAME = 'firstName'
    LAST_NAME = 'lastName'
    PROVISIONING_ALLOWED = 'provisioningAllowed'
    ROLES = 'roles'
    USERNAME = 'username'
    VISIBLE_APPS = 'visibleApps'

class AppClipAdvancedExperienceLocalizationField(StringEnum):
    LANGUAGE = 'language'
    SUBTITLE = 'subtitle'
    TITLE = 'title'

class AppClipDomainStatuseField(StringEnum):
    DOMAINS = 'domains'
    LAST_UPDATED_DATE = 'lastUpdatedDate'

class BetaAppClipInvocationLocalizationField(StringEnum):
    BETA_APP_CLIP_INVOCATION = 'betaAppClipInvocation'
    LOCALE = 'locale'
    TITLE = 'title'

class BuildBundleFileSizeField(StringEnum):
    DEVICE_MODEL = 'deviceModel'
    DOWNLOAD_BYTES = 'downloadBytes'
    INSTALL_BYTES = 'installBytes'
    OS_VERSION = 'osVersion'

class BuildBundleField(StringEnum):
    APP_CLIP_DOMAIN_CACHE_STATUS = 'appClipDomainCacheStatus'
    APP_CLIP_DOMAIN_DEBUG_STATUS = 'appClipDomainDebugStatus'
    BETA_APP_CLIP_INVOCATIONS = 'betaAppClipInvocations'
    BUILD_BUNDLE_FILE_SIZES = 'buildBundleFileSizes'
    BUNDLE_ID = 'bundleId'
    BUNDLE_TYPE = 'bundleType'
    D_SYM_URL = 'dSYMUrl'
    DEVICE_PROTOCOLS = 'deviceProtocols'
    ENTITLEMENTS = 'entitlements'
    FILE_NAME = 'fileName'
    HAS_ON_DEMAND_RESOURCES = 'hasOnDemandResources'
    HAS_PRERENDERED_ICON = 'hasPrerenderedIcon'
    HAS_SIRIKIT = 'hasSirikit'
    INCLUDES_SYMBOLS = 'includesSymbols'
    IS_IOS_BUILD_MAC_APP_STORE_COMPATIBLE = 'isIosBuildMacAppStoreCompatible'
    LOCALES = 'locales'
    PLATFORM_BUILD = 'platformBuild'
    REQUIRED_CAPABILITIES = 'requiredCapabilities'
    SDK_BUILD = 'sdkBuild'
    SUPPORTED_ARCHITECTURES = 'supportedArchitectures'
    USES_LOCATION_SERVICES = 'usesLocationServices'

