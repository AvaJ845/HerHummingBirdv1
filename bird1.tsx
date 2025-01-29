import React, { useState } from 'react';
import { Calculator, RefreshCw, DollarSign, TrendingUp } from 'lucide-react';
import { Alert, AlertTitle, AlertDescription } from '@/components/ui/alert';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

// Constants
const CURRENT_YEAR = new Date().getFullYear();
const ANNUAL_LIMIT = 23000;
const CATCH_UP_LIMIT = 7500;

const TSPCalculator = () => {
  const [activeTab, setActiveTab] = useState('contributions');
  
  const [personalInfo, setPersonalInfo] = useState({
    age: '',
    salary: '',
    yearsOfService: '',
    retirementSystem: 'FERS',
    isSpecialCategory: false,
    stateOfResidence: '',
    taxBracket: '',
    filingStatus: 'single'
  });

  const [accountInfo, setAccountInfo] = useState({
    traditionalBalance: 0,
    rothBalance: 0
  });

  const [contributions, setContributions] = useState({
    traditional: 0,
    roth: 0,
    catchUp: 0,
    agencyMatch: 0,
    agencyAutomatic: 0
  });

  const [fundAllocations, setFundAllocations] = useState({
    gFund: 0,
    fFund: 0,
    cFund: 0,
    sFund: 0,
    iFund: 0,
    lFunds: {
      lIncome: 0,
      l2025: 0,
      l2030: 0,
      l2035: 0,
      l2040: 0,
      l2045: 0,
      l2050: 0,
      l2055: 0,
      l2060: 0,
      l2065: 0
    }
  });

  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');

  // Historical fund performance data
  const fundPerformance = {
    gFund: { return: 2.35, risk: 'Very Low', volatility: 0.5 },
    fFund: { return: 3.45, risk: 'Low', volatility: 4.8 },
    cFund: { return: 11.82, risk: 'Moderate', volatility: 15.2 },
    sFund: { return: 10.54, risk: 'High', volatility: 17.5 },
    iFund: { return: 7.26, risk: 'High', volatility: 16.8 }
  };

  // Tax brackets for 2024
  const taxBrackets = [
    { rate: 0.10, single: 11600, married: 23200 },
    { rate: 0.12, single: 47150, married: 94300 },
    { rate: 0.22, single: 100525, married: 201050 },
    { rate: 0.24, single: 191950, married: 383900 },
    { rate: 0.32, single: 243725, married: 487450 },
    { rate: 0.35, single: 609350, married: 731200 },
    { rate: 0.37, single: Infinity, married: Infinity }
  ];

  // Calculate retirement age
  const calculateRetirementAge = () => {
    const { age, yearsOfService, retirementSystem, isSpecialCategory } = personalInfo;
    
    if (retirementSystem === 'FERS') {
      if (isSpecialCategory) {
        return Math.min(57, Number(age) + (20 - Number(yearsOfService)));
      }
      const birthYear = CURRENT_YEAR - Number(age);
      if (birthYear < 1948) return 55;
      if (birthYear > 1969) return 57;
      return 55 + Math.min(2, (birthYear - 1947) * 0.166667);
    }
    // CSRS
    if (isSpecialCategory) {
      return Math.min(55, Number(age) + (20 - Number(yearsOfService)));
    }
    return Math.min(62, Number(age) + (30 - Number(yearsOfService)));
  };

  // Calculate RMD
  const calculateRMD = (age, balance) => {
    if (age < 73) return 0;
    const distributionPeriod = {
      73: 26.5,
      74: 25.5,
      75: 24.6,
      76: 23.7,
      77: 22.9,
      78: 22.0,
      79: 21.1,
      80: 20.2
    }[age] || 20.2;
    
    return balance / distributionPeriod;
  };

  // Calculate tax implications
  const calculateTaxImplications = () => {
    const marginalRate = taxBrackets.find(bracket => 
      Number(personalInfo.salary) <= bracket[personalInfo.filingStatus]
    )?.rate || 0.37;

    return {
      traditionalSavings: contributions.traditional * marginalRate,
      rothTaxPaid: contributions.roth,
      projectedRMD: calculateRMD(73, accountInfo.traditionalBalance),
      projectedTaxRate: marginalRate
    };
  };

  const handleTabChange = (tab) => setActiveTab(tab);

  return (
    <div className="p-6 max-w-6xl mx-auto">
      <h1 className="text-2xl font-bold mb-6">Federal TSP Calculator</h1>
      
      {/* Tab Navigation */}
      <div className="flex space-x-4 mb-6 border-b">
        {[
          { id: 'personal', label: 'Personal Info', icon: <DollarSign className="w-4 h-4" /> },
          { id: 'contributions', label: 'Contributions', icon: <Calculator className="w-4 h-4" /> },
          { id: 'funds', label: 'Fund Analysis', icon: <TrendingUp className="w-4 h-4" /> },
          { id: 'retirement', label: 'Retirement', icon: <RefreshCw className="w-4 h-4" /> }
        ].map(tab => (
          <button
            key={tab.id}
            onClick={() => handleTabChange(tab.id)}
            className={`flex items-center gap-2 px-4 py-2 border-b-2 ${
              activeTab === tab.id ? 'border-blue-500 text-blue-500' : 'border-transparent'
            }`}
          >
            {tab.icon}
            {tab.label}
          </button>
        ))}
      </div>

      {/* Personal Information Section */}
      {activeTab === 'personal' && (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div className="border rounded-lg p-4">
            <h2 className="text-lg font-semibold mb-4">Basic Information</h2>
            <div className="space-y-4">
              <div>
                <label className="block text-sm font-medium mb-2">Age</label>
                <input
                  type="number"
                  value={personalInfo.age}
                  onChange={e => setPersonalInfo({...personalInfo, age: e.target.value})}
                  className="border rounded p-2 w-full"
                  min="0"
                />
              </div>
              <div>
                <label className="block text-sm font-medium mb-2">Annual Salary</label>
                <input
                  type="number"
                  value={personalInfo.salary}
                  onChange={e => setPersonalInfo({...personalInfo, salary: e.target.value})}
                  className="border rounded p-2 w-full"
                  min="0"
                />
              </div>
              <div>
                <label className="block text-sm font-medium mb-2">Years of Service</label>
                <input
                  type="number"
                  value={personalInfo.yearsOfService}
                  onChange={e => setPersonalInfo({...personalInfo, yearsOfService: e.target.value})}
                  className="border rounded p-2 w-full"
                  min="0"
                />
              </div>
            </div>
          </div>

          <div className="border rounded-lg p-4">
            <h2 className="text-lg font-semibold mb-4">Retirement System</h2>
            <div className="space-y-4">
              <div>
                <label className="block text-sm font-medium mb-2">System</label>
                <select
                  value={personalInfo.retirementSystem}
                  onChange={e => setPersonalInfo({...personalInfo, retirementSystem: e.target.value})}
                  className="border rounded p-2 w-full"
                >
                  <option value="FERS">FERS</option>
                  <option value="CSRS">CSRS</option>
                </select>
              </div>
              <div className="flex items-center">
                <input
                  type="checkbox"
                  checked={personalInfo.isSpecialCategory}
                  onChange={e => setPersonalInfo({...personalInfo, isSpecialCategory: e.target.checked})}
                  className="mr-2"
                />
                <label className="text-sm">Special Category Employee</label>
              </div>
            </div>
          </div>
        </div>
      )}

      {error && (
        <Alert variant="destructive" className="mt-6">
          <AlertTitle>Error</AlertTitle>
          <AlertDescription>{error}</AlertDescription>
        </Alert>
      )}

      {success && (
        <Alert className="mt-6 bg-green-50 border-green-200">
          <AlertTitle>Success</AlertTitle>
          <AlertDescription>{success}</AlertDescription>
        </Alert>
      )}
    </div>
  );
};

export default TSPCalculator;
