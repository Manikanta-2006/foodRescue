import React, { useState } from 'react';
import { useAuth, DEMO_CREDENTIALS } from '../context/AuthContext';
import { X, Sparkles, Building2, Truck, Utensils, ShieldCheck, Mail, Lock, User, Phone, MapPin } from 'lucide-react';

export default function AuthModal({ isOpen, onClose, initialMode = 'login', defaultRole = 'donor' }) {
  const { login, register, quickLogin } = useAuth();
  const [isRegister, setIsRegister] = useState(initialMode === 'register');
  const [role, setRole] = useState(defaultRole);
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    password: '',
    phone: '',
    address: '',
    organizationName: '',
    organizationType: 'Community Kitchen & Food Pantry',
    serviceArea: '',
    transportType: 'car',
    transportCapacityKg: 25
  });
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  if (!isOpen) return null;

  const handleChange = (e) => {
    setFormData(prev => ({ ...prev, [e.target.name]: e.target.value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);

    try {
      if (isRegister) {
        await register({ ...formData, role });
      } else {
        await login(formData.email, formData.password);
      }
      onClose();
    } catch (err) {
      setError(err.message || 'Authentication failed');
    } finally {
      setLoading(false);
    }
  };

  const handleQuickLogin = async (roleKey) => {
    setError('');
    setLoading(true);
    try {
      await quickLogin(roleKey);
      onClose();
    } catch (err) {
      setError(err.message || 'Demo login failed');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="fixed inset-0 z-50 overflow-y-auto bg-warm-900/60 backdrop-blur-sm flex items-center justify-center p-4">
      <div className="bg-white rounded-2xl shadow-2xl max-w-md w-full overflow-hidden border border-warm-200 animate-in fade-in zoom-in-95 duration-150">
        {/* Header */}
        <div className="bg-gradient-to-r from-brand-700 to-brand-600 px-6 py-5 text-white flex justify-between items-center">
          <div>
            <h3 className="text-lg font-bold">
              {isRegister ? 'Join FoodRescue India' : 'Welcome Back'}
            </h3>
            <p className="text-xs text-brand-100">
              {isRegister ? 'Create an account to begin rescuing food' : 'Sign in to access your portal'}
            </p>
          </div>
          <button onClick={onClose} className="text-white/80 hover:text-white p-1 rounded-lg hover:bg-white/10">
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Content */}
        <div className="p-6">
          {error && (
            <div className="mb-4 p-3 rounded-lg bg-rose-50 border border-rose-200 text-rose-700 text-xs">
              {error}
            </div>
          )}

          {/* Tab Switcher */}
          <div className="flex bg-warm-100 p-1 rounded-xl mb-5">
            <button
              type="button"
              onClick={() => { setIsRegister(false); setError(''); }}
              className={`flex-1 py-1.5 text-xs font-semibold rounded-lg transition ${
                !isRegister ? 'bg-white text-warm-900 shadow-sm' : 'text-warm-500 hover:text-warm-900'
              }`}
            >
              Sign In
            </button>
            <button
              type="button"
              onClick={() => { setIsRegister(true); setError(''); }}
              className={`flex-1 py-1.5 text-xs font-semibold rounded-lg transition ${
                isRegister ? 'bg-white text-warm-900 shadow-sm' : 'text-warm-500 hover:text-warm-900'
              }`}
            >
              Create Account
            </button>
          </div>

          <form onSubmit={handleSubmit} className="space-y-3.5">
            {isRegister && (
              <>
                {/* Role Selector */}
                <div>
                  <label className="block text-xs font-semibold text-warm-700 mb-1.5">Select Role</label>
                  <div className="grid grid-cols-3 gap-2">
                    {[
                      { key: 'donor', label: 'Donor', icon: Utensils },
                      { key: 'ngo', label: 'NGO/Shelter', icon: Building2 },
                      { key: 'volunteer', label: 'Volunteer', icon: Truck },
                    ].map(r => {
                      const Icon = r.icon;
                      return (
                        <button
                          key={r.key}
                          type="button"
                          onClick={() => setRole(r.key)}
                          className={`p-2 rounded-xl border text-center transition flex flex-col items-center justify-center space-y-1 ${
                            role === r.key
                              ? 'border-brand-600 bg-brand-50 text-brand-800 font-bold shadow-sm'
                              : 'border-warm-200 hover:bg-warm-50 text-warm-600'
                          }`}
                        >
                          <Icon className="w-4 h-4" />
                          <span className="text-[11px]">{r.label}</span>
                        </button>
                      );
                    })}
                  </div>
                </div>

                <div>
                  <label className="block text-xs font-medium text-warm-700 mb-1">
                    {role === 'ngo' ? 'Representative Name' : 'Full Name'}
                  </label>
                  <div className="relative">
                    <User className="w-4 h-4 text-warm-400 absolute left-3 top-2.5" />
                    <input
                      name="name"
                      required
                      value={formData.name}
                      onChange={handleChange}
                      placeholder="e.g. Rahul Sharma"
                      className="w-full pl-9 pr-3 py-2 text-xs border border-warm-300 rounded-lg focus:ring-2 focus:ring-brand-500 focus:outline-none"
                    />
                  </div>
                </div>

                {role === 'ngo' && (
                  <div>
                    <label className="block text-xs font-medium text-warm-700 mb-1">Organization Name</label>
                    <div className="relative">
                      <Building2 className="w-4 h-4 text-warm-400 absolute left-3 top-2.5" />
                      <input
                        name="organizationName"
                        required
                        value={formData.organizationName}
                        onChange={handleChange}
                        placeholder="e.g. Roti Bank Seva Trust"
                        className="w-full pl-9 pr-3 py-2 text-xs border border-warm-300 rounded-lg focus:ring-2 focus:ring-brand-500 focus:outline-none"
                      />
                    </div>
                  </div>
                )}
              </>
            )}

            <div>
              <label className="block text-xs font-medium text-warm-700 mb-1">Email Address</label>
              <div className="relative">
                <Mail className="w-4 h-4 text-warm-400 absolute left-3 top-2.5" />
                <input
                  type="email"
                  name="email"
                  required
                  value={formData.email}
                  onChange={handleChange}
                  placeholder="e.g. rahul.sharma@example.in"
                  className="w-full pl-9 pr-3 py-2 text-xs border border-warm-300 rounded-lg focus:ring-2 focus:ring-brand-500 focus:outline-none"
                />
              </div>
            </div>

            <div>
              <label className="block text-xs font-medium text-warm-700 mb-1">Password</label>
              <div className="relative">
                <Lock className="w-4 h-4 text-warm-400 absolute left-3 top-2.5" />
                <input
                  type="password"
                  name="password"
                  required
                  value={formData.password}
                  onChange={handleChange}
                  placeholder="••••••••"
                  className="w-full pl-9 pr-3 py-2 text-xs border border-warm-300 rounded-lg focus:ring-2 focus:ring-brand-500 focus:outline-none"
                />
              </div>
            </div>

            {isRegister && (
              <>
                <div className="grid grid-cols-2 gap-2">
                  <div>
                    <label className="block text-xs font-medium text-warm-700 mb-1">Mobile (+91)</label>
                    <input
                      name="phone"
                      value={formData.phone}
                      onChange={handleChange}
                      placeholder="+91-98765-43210"
                      className="w-full px-3 py-2 text-xs border border-warm-300 rounded-lg focus:ring-2 focus:ring-brand-500 focus:outline-none"
                    />
                  </div>
                  <div>
                    <label className="block text-xs font-medium text-warm-700 mb-1">Location / Area</label>
                    <input
                      name="address"
                      value={formData.address}
                      onChange={handleChange}
                      placeholder="Indiranagar, Bengaluru"
                      className="w-full px-3 py-2 text-xs border border-warm-300 rounded-lg focus:ring-2 focus:ring-brand-500 focus:outline-none"
                    />
                  </div>
                </div>

                {role === 'volunteer' && (
                  <div className="grid grid-cols-2 gap-2">
                    <div>
                      <label className="block text-xs font-medium text-warm-700 mb-1">Transport</label>
                      <select
                        name="transportType"
                        value={formData.transportType}
                        onChange={handleChange}
                        className="w-full px-3 py-2 text-xs border border-warm-300 rounded-lg focus:ring-2 focus:ring-brand-500 focus:outline-none"
                      >
                        <option value="walking">Walking</option>
                        <option value="bicycle">Bicycle</option>
                        <option value="motorcycle">Motorcycle</option>
                        <option value="car">Car</option>
                        <option value="van">Van</option>
                      </select>
                    </div>
                    <div>
                      <label className="block text-xs font-medium text-warm-700 mb-1">Max Capacity (kg)</label>
                      <input
                        type="number"
                        name="transportCapacityKg"
                        value={formData.transportCapacityKg}
                        onChange={handleChange}
                        className="w-full px-3 py-2 text-xs border border-warm-300 rounded-lg focus:ring-2 focus:ring-brand-500 focus:outline-none"
                      />
                    </div>
                  </div>
                )}
              </>
            )}

            <button
              type="submit"
              disabled={loading}
              className="w-full py-2.5 px-4 bg-brand-600 hover:bg-brand-700 disabled:opacity-50 text-white font-semibold text-xs rounded-xl shadow-md shadow-brand-600/30 transition mt-2"
            >
              {loading ? 'Please wait...' : isRegister ? 'Register Account' : 'Sign In'}
            </button>
          </form>

          {/* Quick Demo Sign-In Card */}
          <div className="mt-5 pt-4 border-t border-warm-200">
            <div className="flex items-center space-x-1.5 text-xs font-bold text-warm-600 mb-2.5">
              <Sparkles className="w-3.5 h-3.5 text-amber-500" />
              <span>1-Click Indian Demo Logins</span>
            </div>
            <div className="grid grid-cols-2 gap-2">
              <button
                type="button"
                onClick={() => handleQuickLogin('admin')}
                className="p-2 rounded-lg bg-warm-100 hover:bg-warm-200 text-left transition border border-warm-200 text-[11px]"
              >
                <div className="font-semibold text-warm-800 flex items-center space-x-1">
                  <ShieldCheck className="w-3 h-3 text-purple-600" />
                  <span>Admin</span>
                </div>
                <div className="text-[10px] text-warm-500">Vikram Malhotra</div>
              </button>

              <button
                type="button"
                onClick={() => handleQuickLogin('donor')}
                className="p-2 rounded-lg bg-warm-100 hover:bg-warm-200 text-left transition border border-warm-200 text-[11px]"
              >
                <div className="font-semibold text-warm-800 flex items-center space-x-1">
                  <Utensils className="w-3 h-3 text-brand-600" />
                  <span>Donor</span>
                </div>
                <div className="text-[10px] text-warm-500">Annapurna Grand</div>
              </button>

              <button
                type="button"
                onClick={() => handleQuickLogin('ngo')}
                className="p-2 rounded-lg bg-warm-100 hover:bg-warm-200 text-left transition border border-warm-200 text-[11px]"
              >
                <div className="font-semibold text-warm-800 flex items-center space-x-1">
                  <Building2 className="w-3 h-3 text-blue-600" />
                  <span>NGO / Shelter</span>
                </div>
                <div className="text-[10px] text-warm-500">Roti Bank Seva</div>
              </button>

              <button
                type="button"
                onClick={() => handleQuickLogin('volunteer')}
                className="p-2 rounded-lg bg-warm-100 hover:bg-warm-200 text-left transition border border-warm-200 text-[11px]"
              >
                <div className="font-semibold text-warm-800 flex items-center space-x-1">
                  <Truck className="w-3 h-3 text-amber-600" />
                  <span>Volunteer</span>
                </div>
                <div className="text-[10px] text-warm-500">Aarav Sharma (Courier)</div>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
