""" The ToolValidator classes is for ArcToolbox script tool dialog validation.
    
"""

from . import BaseValidators
from ATtILA2.constants import metricConstants
#import pylet.lcc.constants as lccConstants
from  ATtILA2.utils.lcc import constants as lccConstants
#from  .utils.lcc import constants as lccConstants
from ATtILA2.constants.metricConstants import *

class lcospToolValidator(BaseValidators.ProportionsValidator):
    """Tool Validator for LandCoverSlopeOverlap"""
    
    filterList = lcospConstants.optionalFilter
    overrideAttributeName = lccConstants.XmlAttributeLcospField
    fieldPrefix = lcospConstants.fieldPrefix
    fieldSuffix = lcospConstants.fieldSuffix
    metricShortName = lcospConstants.shortName

class flcpToolValidator(BaseValidators.ProportionsValidator):
    """Tool Validator for FloodplainLandCoverProportion"""
      
    filterList = flcpConstants.optionalFilter
    overrideAttributeName = lccConstants.XmlAttributeLcpField
    fieldPrefix = flcpConstants.fieldPrefix
    fieldSuffix = flcpConstants.fieldSuffix
    metricShortName = flcpConstants.shortName
    
class lcpToolValidator(BaseValidators.ProportionsValidator):
    """ ToolValidator for LandCoverProportions """
    
    filterList = lcpConstants.optionalFilter
    overrideAttributeName = lccConstants.XmlAttributeLcpField
    fieldPrefix = lcpConstants.fieldPrefix
    fieldSuffix = lcpConstants.fieldSuffix    
    metricShortName = lcpConstants.shortName 
    
class lcppcToolValidator(BaseValidators.ProportionsValidator):
    """ ToolValidator for LandCoverProportions """
    
    filterList = lcppcConstants.optionalFilter
    overrideAttributeName = lccConstants.XmlAttributeLcpField
    fieldPrefix = lcppcConstants.fieldPrefix
    fieldSuffix = lcppcConstants.fieldSuffix    
    metricShortName = lcppcConstants.shortName 

class lcccToolValidator(BaseValidators.CoefficientValidator):
    """ ToolValidator for Coefficient Calculations """
    filterList = lcccConstants.optionalFilter
    overrideAttributeName = lccConstants.XmlAttributeLcpField
    fieldPrefix = lcccConstants.fieldPrefix
    fieldSuffix = lcccConstants.fieldSuffix    
    metricShortName = lcccConstants.shortName 
    
class rlcpToolValidator(BaseValidators.ProportionsValidator):
    """ ToolValidator for RiparianLandCoverProportions"""
    
    filterList = rlcpConstants.optionalFilter
    overrideAttributeName = lccConstants.XmlAttributeRlcpField
    fieldPrefix = rlcpConstants.fieldPrefix
    fieldSuffix = rlcpConstants.fieldSuffix
    metricShortName = rlcpConstants.shortName
    
class splcpToolValidator(BaseValidators.ProportionsValidator):
    """ ToolValidator for SamplePointLandCoverProportions"""
    
    filterList = splcpConstants.optionalFilter
    overrideAttributeName = lccConstants.XmlAttributeSplcpField
    fieldPrefix = splcpConstants.fieldPrefix
    fieldSuffix = splcpConstants.fieldSuffix
    metricShortName = splcpConstants.shortName
    
class caemToolValidator(BaseValidators.ProportionsValidator):
    """ ToolValidator for CoreAndEdgeMetrics """
    
    filterList = caemConstants.optionalFilter
#    overrideAttributeName = lccConstants.XmlAttributeCaemField
    fieldPrefix = caemConstants.fieldPrefix
    fieldSuffix = caemConstants.fieldSuffix    
    metricShortName = caemConstants.shortName
    
class rdmToolValidator(BaseValidators.NoLccFileValidator):
    """ ToolValidator for RoadDensityMetrics """
    
    filterList = rdmConstants.optionalFilter
    fieldPrefix = rdmConstants.fieldPrefix
    fieldSuffix = rdmConstants.fieldSuffix    
    metricShortName = rdmConstants.shortName
    
class lcdToolValidator(BaseValidators.NoLccFileValidator):
    """ ToolValidator for LandCoverDiversity """
    
    filterList = lcdConstants.optionalFilter
    fieldPrefix = lcdConstants.fieldPrefix
    fieldSuffix = lcdConstants.fieldSuffix
    metricShortName = lcdConstants.shortName
    
class pdmToolValidator(BaseValidators.NoLccFileValidator):
    """ ToolValidator for PopulationDensityMetrics """
    
    filterList = pdmConstants.optionalFilter
    fieldPrefix = pdmConstants.fieldPrefix
    fieldSuffix = pdmConstants.fieldSuffix
    metricShortName = pdmConstants.shortName
    
class pifmToolValidator(BaseValidators.NoLccFileValidator):
    """ ToolValidator for PopulationInFloodplainMetrics """
    
    filterList = pdmConstants.optionalFilter
    fieldPrefix = pdmConstants.fieldPrefix
    fieldSuffix = pdmConstants.fieldSuffix
    metricShortName = pdmConstants.shortName
    
class pmToolValidator(BaseValidators.ProportionsValidator):
    """ ToolValidator for PatchMetrics """
    
    filterList = pmConstants.optionalFilter
#    overrideAttributeName = lccConstants.XmlAttributePmField
    fieldPrefix = pmConstants.fieldPrefix
    fieldSuffix = pmConstants.fieldSuffix
    metricShortName = pmConstants.shortName

class gppToolValidator(BaseValidators.NoReportingUnitValidator):
    """ ToolValidator for GenerateProximityPolygon Utility """
    
    filterList = gppConstants.optionalFilter
#    overrideAttributeName = lccConstants.XmlAttributePmField
#    fieldPrefix = pmConstants.fieldPrefix
#    fieldSuffix = pmConstants.fieldSuffix
    metricShortName = gppConstants.shortName


