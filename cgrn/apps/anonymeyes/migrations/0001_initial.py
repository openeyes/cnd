# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models
from uuid import UUID


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DOBPrecision'
        db.create_table('anonymeyes_dobprecision', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('sort', self.gf('django.db.models.fields.IntegerField')(default=10)),
        ))
        db.send_create_signal('cndapp', ['DOBPrecision'])

        # Adding model 'UserProfile'
        db.create_table('anonymeyes_userprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('dob_precision', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['cndapp.DOBPrecision'])),
        ))
        db.send_create_signal('cndapp', ['UserProfile'])

        # Adding model 'EthnicGroup'
        db.create_table('anonymeyes_ethnicgroup', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('sort', self.gf('django.db.models.fields.IntegerField')(default=10)),
        ))
        db.send_create_signal('cndapp', ['EthnicGroup'])

        # Adding model 'Eye'
        db.create_table('anonymeyes_eye', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('single', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('sort', self.gf('django.db.models.fields.IntegerField')(default=10)),
        ))
        db.send_create_signal('cndapp', ['Eye'])

        # Adding model 'DiagnosisGroup'
        db.create_table('anonymeyes_diagnosisgroup', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('sort', self.gf('django.db.models.fields.IntegerField')(default=10)),
        ))
        db.send_create_signal('cndapp', ['DiagnosisGroup'])

        # Adding model 'Diagnosis'
        db.create_table('anonymeyes_diagnosis', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cndapp.DiagnosisGroup'])),
            ('sort', self.gf('django.db.models.fields.IntegerField')(default=10)),
        ))
        db.send_create_signal('cndapp', ['Diagnosis'])

        # Adding model 'HealthCare'
        db.create_table('anonymeyes_healthcare', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('sort', self.gf('django.db.models.fields.IntegerField')(default=10)),
        ))
        db.send_create_signal('cndapp', ['HealthCare'])

        # Adding model 'Anaesthesia'
        db.create_table('anonymeyes_anaesthesia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('sort', self.gf('django.db.models.fields.IntegerField')(default=10)),
        ))
        db.send_create_signal('cndapp', ['Anaesthesia'])

        # Adding model 'LensStatus'
        db.create_table('anonymeyes_lensstatus', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal('cndapp', ['LensStatus'])

        # Adding model 'VisualAcuityScale'
        db.create_table('anonymeyes_visualacuityscale', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('sort', self.gf('django.db.models.fields.IntegerField')(default=10)),
        ))
        db.send_create_signal('cndapp', ['VisualAcuityScale'])

        # Adding model 'VisualAcuityMethod'
        db.create_table('anonymeyes_visualacuitymethod', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('sort', self.gf('django.db.models.fields.IntegerField')(default=10)),
            ('scale', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cndapp.VisualAcuityScale'])),
        ))
        db.send_create_signal('cndapp', ['VisualAcuityMethod'])

        # Adding model 'VisualAcuityReading'
        db.create_table('anonymeyes_visualacuityreading', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
            ('sort', self.gf('django.db.models.fields.IntegerField')(default=10)),
            ('scale', self.gf('django.db.models.fields.related.ForeignKey')(related_name='readings', to=orm['cndapp.VisualAcuityScale'])),
        ))
        db.send_create_signal('cndapp', ['VisualAcuityReading'])

        # Adding model 'VisualAcuityCorrection'
        db.create_table('anonymeyes_visualacuitycorrection', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('sort', self.gf('django.db.models.fields.IntegerField')(default=10)),
        ))
        db.send_create_signal('cndapp', ['VisualAcuityCorrection'])

        # Adding model 'Tonometry'
        db.create_table('anonymeyes_tonometry', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('sort', self.gf('django.db.models.fields.IntegerField')(default=10)),
        ))
        db.send_create_signal('cndapp', ['Tonometry'])

        # Adding model 'Patient'
        db.create_table('anonymeyes_patient', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uuid', self.gf('django.db.models.fields.CharField')(default=UUID('3ccecfc6-56a0-4350-b346-589e4048dfdd'), unique=True, max_length=64, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='patient_created_set', null=True, on_delete=models.SET_NULL, to=orm['auth.User'])),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='patient_updated_set', null=True, on_delete=models.SET_NULL, to=orm['auth.User'])),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('sex', self.gf('django.db.models.fields.IntegerField')()),
            ('dob_day', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('dob_month', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('dob_year', self.gf('django.db.models.fields.IntegerField')()),
            ('postcode', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('health_care', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cndapp.HealthCare'])),
            ('ethnic_group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cndapp.EthnicGroup'])),
            ('consanguinity', self.gf('django.db.models.fields.IntegerField')()),
            ('diagnosis_right', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['cndapp.Diagnosis'])),
            ('diagnosis_left', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['cndapp.Diagnosis'])),
            ('lens_status_right', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['cndapp.LensStatus'])),
            ('lens_status_left', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['cndapp.LensStatus'])),
            ('lens_extraction_date_right', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('lens_extraction_date_left', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('visual_acuity_date', self.gf('django.db.models.fields.DateField')()),
            ('visual_acuity_method', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cndapp.VisualAcuityMethod'])),
            ('visual_acuity_right', self.gf('django.db.models.fields.related.ForeignKey')(related_name='patient_rva', to=orm['cndapp.VisualAcuityReading'])),
            ('visual_acuity_left', self.gf('django.db.models.fields.related.ForeignKey')(related_name='patient_lva', to=orm['cndapp.VisualAcuityReading'])),
            ('visual_acuity_both', self.gf('django.db.models.fields.related.ForeignKey')(related_name='patient_beo', to=orm['cndapp.VisualAcuityReading'])),
            ('visual_acuity_correction_right', self.gf('django.db.models.fields.related.ForeignKey')(related_name='patient_rva_correction', to=orm['cndapp.VisualAcuityCorrection'])),
            ('visual_acuity_correction_left', self.gf('django.db.models.fields.related.ForeignKey')(related_name='patient_lva_correction', to=orm['cndapp.VisualAcuityCorrection'])),
            ('visual_acuity_correction_both', self.gf('django.db.models.fields.related.ForeignKey')(related_name='patient_beo_correction', to=orm['cndapp.VisualAcuityCorrection'])),
            ('iop_right', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('iop_left', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('tonometry', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cndapp.Tonometry'])),
            ('eua', self.gf('django.db.models.fields.IntegerField')()),
            ('anaesthesia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cndapp.Anaesthesia'], null=True, blank=True)),
        ))
        db.send_create_signal('cndapp', ['Patient'])

        # Adding model 'Complication'
        db.create_table('anonymeyes_complication', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('sort', self.gf('django.db.models.fields.IntegerField')(default=10)),
        ))
        db.send_create_signal('cndapp', ['Complication'])

        # Adding model 'Surgery'
        db.create_table('anonymeyes_surgery', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('adjuvant', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('stage', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('sort', self.gf('django.db.models.fields.IntegerField')(default=10)),
        ))
        db.send_create_signal('cndapp', ['Surgery'])

        # Adding model 'Adjuvant'
        db.create_table('anonymeyes_adjuvant', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('sort', self.gf('django.db.models.fields.IntegerField')(default=10)),
        ))
        db.send_create_signal('cndapp', ['Adjuvant'])

        # Adding model 'SurgeryStage'
        db.create_table('anonymeyes_surgerystage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('sort', self.gf('django.db.models.fields.IntegerField')(default=10)),
        ))
        db.send_create_signal('cndapp', ['SurgeryStage'])

        # Adding model 'ManagementType'
        db.create_table('anonymeyes_managementtype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('sort', self.gf('django.db.models.fields.IntegerField')(default=10)),
        ))
        db.send_create_signal('cndapp', ['ManagementType'])

        # Adding model 'Management'
        db.create_table('anonymeyes_management', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='management_created_set', null=True, on_delete=models.SET_NULL, to=orm['auth.User'])),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='management_updated_set', null=True, on_delete=models.SET_NULL, to=orm['auth.User'])),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('eye', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cndapp.Eye'], null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cndapp.ManagementType'])),
            ('surgery', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cndapp.Surgery'], null=True, blank=True)),
            ('complication', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cndapp.Complication'], null=True, blank=True)),
            ('adjuvant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cndapp.Adjuvant'], null=True, blank=True)),
            ('surgery_stage', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cndapp.SurgeryStage'], null=True, blank=True)),
            ('comments', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('patient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cndapp.Patient'])),
        ))
        db.send_create_signal('cndapp', ['Management'])

        # Adding model 'Outcome'
        db.create_table('anonymeyes_outcome', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='outcome_created_set', null=True, on_delete=models.SET_NULL, to=orm['auth.User'])),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='outcome_updated_set', null=True, on_delete=models.SET_NULL, to=orm['auth.User'])),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('eye', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cndapp.Eye'])),
            ('iop_control', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('iop_agents', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('visual_acuity_method', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cndapp.VisualAcuityMethod'])),
            ('visual_acuity_right', self.gf('django.db.models.fields.related.ForeignKey')(related_name='outcome_rva', to=orm['cndapp.VisualAcuityReading'])),
            ('visual_acuity_left', self.gf('django.db.models.fields.related.ForeignKey')(related_name='outcome_lva', to=orm['cndapp.VisualAcuityReading'])),
            ('visual_acuity_both', self.gf('django.db.models.fields.related.ForeignKey')(related_name='outcome_beo', to=orm['cndapp.VisualAcuityReading'])),
            ('visual_acuity_correction_right', self.gf('django.db.models.fields.related.ForeignKey')(related_name='outcome_rva_correction', to=orm['cndapp.VisualAcuityCorrection'])),
            ('visual_acuity_correction_left', self.gf('django.db.models.fields.related.ForeignKey')(related_name='outcome_lva_correction', to=orm['cndapp.VisualAcuityCorrection'])),
            ('visual_acuity_correction_both', self.gf('django.db.models.fields.related.ForeignKey')(related_name='outcome_beo_correction', to=orm['cndapp.VisualAcuityCorrection'])),
            ('patient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cndapp.Patient'])),
        ))
        db.send_create_signal('cndapp', ['Outcome'])


    def backwards(self, orm):
        # Deleting model 'DOBPrecision'
        db.delete_table('anonymeyes_dobprecision')

        # Deleting model 'UserProfile'
        db.delete_table('anonymeyes_userprofile')

        # Deleting model 'EthnicGroup'
        db.delete_table('anonymeyes_ethnicgroup')

        # Deleting model 'Eye'
        db.delete_table('anonymeyes_eye')

        # Deleting model 'DiagnosisGroup'
        db.delete_table('anonymeyes_diagnosisgroup')

        # Deleting model 'Diagnosis'
        db.delete_table('anonymeyes_diagnosis')

        # Deleting model 'HealthCare'
        db.delete_table('anonymeyes_healthcare')

        # Deleting model 'Anaesthesia'
        db.delete_table('anonymeyes_anaesthesia')

        # Deleting model 'LensStatus'
        db.delete_table('anonymeyes_lensstatus')

        # Deleting model 'VisualAcuityScale'
        db.delete_table('anonymeyes_visualacuityscale')

        # Deleting model 'VisualAcuityMethod'
        db.delete_table('anonymeyes_visualacuitymethod')

        # Deleting model 'VisualAcuityReading'
        db.delete_table('anonymeyes_visualacuityreading')

        # Deleting model 'VisualAcuityCorrection'
        db.delete_table('anonymeyes_visualacuitycorrection')

        # Deleting model 'Tonometry'
        db.delete_table('anonymeyes_tonometry')

        # Deleting model 'Patient'
        db.delete_table('anonymeyes_patient')

        # Deleting model 'Complication'
        db.delete_table('anonymeyes_complication')

        # Deleting model 'Surgery'
        db.delete_table('anonymeyes_surgery')

        # Deleting model 'Adjuvant'
        db.delete_table('anonymeyes_adjuvant')

        # Deleting model 'SurgeryStage'
        db.delete_table('anonymeyes_surgerystage')

        # Deleting model 'ManagementType'
        db.delete_table('anonymeyes_managementtype')

        # Deleting model 'Management'
        db.delete_table('anonymeyes_management')

        # Deleting model 'Outcome'
        db.delete_table('anonymeyes_outcome')


    models = {
        'cndapp.adjuvant': {
            'Meta': {'ordering': "['sort', 'name']", 'object_name': 'Adjuvant'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '10'})
        },
        'cndapp.anaesthesia': {
            'Meta': {'ordering': "['sort', 'name']", 'object_name': 'Anaesthesia'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '10'})
        },
        'cndapp.complication': {
            'Meta': {'ordering': "['sort', 'name']", 'object_name': 'Complication'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '10'})
        },
        'cndapp.diagnosis': {
            'Meta': {'ordering': "['group__sort', 'sort', 'name']", 'object_name': 'Diagnosis'},
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cndapp.DiagnosisGroup']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '10'})
        },
        'cndapp.diagnosisgroup': {
            'Meta': {'ordering': "['sort', 'name']", 'object_name': 'DiagnosisGroup'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '10'})
        },
        'cndapp.dobprecision': {
            'Meta': {'ordering': "['sort', 'name']", 'object_name': 'DOBPrecision'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '10'})
        },
        'cndapp.ethnicgroup': {
            'Meta': {'ordering': "['sort', 'name']", 'object_name': 'EthnicGroup'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '10'})
        },
        'cndapp.eye': {
            'Meta': {'ordering': "['sort', 'name']", 'object_name': 'Eye'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'single': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '10'})
        },
        'cndapp.healthcare': {
            'Meta': {'ordering': "['sort', 'name']", 'object_name': 'HealthCare'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '10'})
        },
        'cndapp.lensstatus': {
            'Meta': {'object_name': 'LensStatus'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'cndapp.management': {
            'Meta': {'object_name': 'Management'},
            'adjuvant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cndapp.Adjuvant']", 'null': 'True', 'blank': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'complication': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cndapp.Complication']", 'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'management_created_set'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['auth.User']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'eye': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cndapp.Eye']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cndapp.Patient']"}),
            'surgery': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cndapp.Surgery']", 'null': 'True', 'blank': 'True'}),
            'surgery_stage': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cndapp.SurgeryStage']", 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cndapp.ManagementType']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'management_updated_set'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['auth.User']"})
        },
        'cndapp.managementtype': {
            'Meta': {'ordering': "['sort', 'name']", 'object_name': 'ManagementType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '10'})
        },
        'cndapp.outcome': {
            'Meta': {'object_name': 'Outcome'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'outcome_created_set'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['auth.User']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'eye': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cndapp.Eye']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iop_agents': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'iop_control': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cndapp.Patient']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'outcome_updated_set'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['auth.User']"}),
            'visual_acuity_both': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'outcome_beo'", 'to': "orm['cndapp.VisualAcuityReading']"}),
            'visual_acuity_correction_both': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'outcome_beo_correction'", 'to': "orm['cndapp.VisualAcuityCorrection']"}),
            'visual_acuity_correction_left': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'outcome_lva_correction'", 'to': "orm['cndapp.VisualAcuityCorrection']"}),
            'visual_acuity_correction_right': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'outcome_rva_correction'", 'to': "orm['cndapp.VisualAcuityCorrection']"}),
            'visual_acuity_left': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'outcome_lva'", 'to': "orm['cndapp.VisualAcuityReading']"}),
            'visual_acuity_method': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cndapp.VisualAcuityMethod']"}),
            'visual_acuity_right': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'outcome_rva'", 'to': "orm['cndapp.VisualAcuityReading']"})
        },
        'cndapp.patient': {
            'Meta': {'ordering': "['-updated_at']", 'object_name': 'Patient'},
            'anaesthesia': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cndapp.Anaesthesia']", 'null': 'True', 'blank': 'True'}),
            'consanguinity': ('django.db.models.fields.IntegerField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'patient_created_set'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['auth.User']"}),
            'diagnosis_left': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['cndapp.Diagnosis']"}),
            'diagnosis_right': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['cndapp.Diagnosis']"}),
            'dob_day': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dob_month': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dob_year': ('django.db.models.fields.IntegerField', [], {}),
            'ethnic_group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cndapp.EthnicGroup']"}),
            'eua': ('django.db.models.fields.IntegerField', [], {}),
            'health_care': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cndapp.HealthCare']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iop_left': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'iop_right': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'lens_extraction_date_left': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'lens_extraction_date_right': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'lens_status_left': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['cndapp.LensStatus']"}),
            'lens_status_right': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['cndapp.LensStatus']"}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'sex': ('django.db.models.fields.IntegerField', [], {}),
            'tonometry': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cndapp.Tonometry']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'patient_updated_set'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['auth.User']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "UUID('66f07409-2c08-43a8-9552-3be7b7bcd8f6')", 'unique': 'True', 'max_length': '64', 'blank': 'True'}),
            'visual_acuity_both': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'patient_beo'", 'to': "orm['cndapp.VisualAcuityReading']"}),
            'visual_acuity_correction_both': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'patient_beo_correction'", 'to': "orm['cndapp.VisualAcuityCorrection']"}),
            'visual_acuity_correction_left': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'patient_lva_correction'", 'to': "orm['cndapp.VisualAcuityCorrection']"}),
            'visual_acuity_correction_right': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'patient_rva_correction'", 'to': "orm['cndapp.VisualAcuityCorrection']"}),
            'visual_acuity_date': ('django.db.models.fields.DateField', [], {}),
            'visual_acuity_left': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'patient_lva'", 'to': "orm['cndapp.VisualAcuityReading']"}),
            'visual_acuity_method': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cndapp.VisualAcuityMethod']"}),
            'visual_acuity_right': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'patient_rva'", 'to': "orm['cndapp.VisualAcuityReading']"})
        },
        'cndapp.surgery': {
            'Meta': {'ordering': "['sort', 'name']", 'object_name': 'Surgery'},
            'adjuvant': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'stage': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'cndapp.surgerystage': {
            'Meta': {'ordering': "['sort', 'name']", 'object_name': 'SurgeryStage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '10'})
        },
        'cndapp.tonometry': {
            'Meta': {'ordering': "['sort', 'name']", 'object_name': 'Tonometry'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '10'})
        },
        'cndapp.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'dob_precision': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': "orm['cndapp.DOBPrecision']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'cndapp.visualacuitycorrection': {
            'Meta': {'ordering': "['sort', 'name']", 'object_name': 'VisualAcuityCorrection'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '10'})
        },
        'cndapp.visualacuitymethod': {
            'Meta': {'ordering': "['sort', 'name']", 'object_name': 'VisualAcuityMethod'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'scale': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cndapp.VisualAcuityScale']"}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '10'})
        },
        'cndapp.visualacuityreading': {
            'Meta': {'ordering': "['scale__name', 'sort', 'name']", 'object_name': 'VisualAcuityReading'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'scale': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'readings'", 'to': "orm['cndapp.VisualAcuityScale']"}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        'cndapp.visualacuityscale': {
            'Meta': {'ordering': "['sort', 'name']", 'object_name': 'VisualAcuityScale'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '10'})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['cndapp']