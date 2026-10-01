import pytest
from pydantic import ValidationError

from ai_systems_lab.config import Settings


@pytest.fixture(autouse=True)
def isolated_settings_environment(monkeypatch, tmp_path):
    """Keep settings tests independent of the user's environment and project .env."""
    monkeypatch.chdir(tmp_path)
    for name in ('GEMINI_API_KEY', 'APP_NAME', 'ENVIRONMENT', 'DEBUG'):
        monkeypatch.delenv(name, raising=False)


class TestSettings:
    def test_settings_loads_gemini_api_key_from_environment(self, monkeypatch):
        # arrange
        monkeypatch.setenv('GEMINI_API_KEY', 'environment-key')

        # act
        settings = Settings()

        # assert
        assert settings.gemini_api_key == 'environment-key'

    def test_settings_rejects_missing_gemini_api_key(self):
        # act
        with pytest.raises(ValidationError) as exc_info:
            Settings()

        # assert
        assert any(
            error['loc'] == ('GEMINI_API_KEY',) and error['type'] == 'missing'
            for error in exc_info.value.errors()
        )

    def test_settings_rejects_empty_gemini_api_key(self, monkeypatch):
        # arrange
        monkeypatch.setenv('GEMINI_API_KEY', '')

        # act
        with pytest.raises(ValidationError) as exc_info:
            Settings()

        # assert
        assert any(
            error['loc'] == ('GEMINI_API_KEY',) and error['type'] == 'string_too_short'
            for error in exc_info.value.errors()
        )

    def test_settings_uses_default_values(self, monkeypatch):
        # arrange
        monkeypatch.setenv('GEMINI_API_KEY', 'test-key')

        # act
        settings = Settings()

        # assert
        assert settings.app_name == 'AI Systems Lab'
        assert settings.environment == 'local'
        assert settings.debug is False

    def test_settings_loads_optional_values_from_environment(self, monkeypatch):
        # arrange
        monkeypatch.setenv('GEMINI_API_KEY', 'test-key')
        monkeypatch.setenv('APP_NAME', 'Custom Lab')
        monkeypatch.setenv('ENVIRONMENT', 'staging')
        monkeypatch.setenv('DEBUG', 'true')

        # act
        settings = Settings()

        # assert
        assert settings.app_name == 'Custom Lab'
        assert settings.environment == 'staging'
        assert settings.debug is True

    def test_settings_loads_gemini_api_key_from_dotenv_file(self, tmp_path):
        # arrange
        (tmp_path / '.env').write_text('GEMINI_API_KEY=dotenv-key\n', encoding='utf-8')

        # act
        settings = Settings()

        # assert
        assert settings.gemini_api_key == 'dotenv-key'

    def test_environment_variable_overrides_dotenv_key(self, monkeypatch, tmp_path):
        # arrange
        (tmp_path / '.env').write_text('GEMINI_API_KEY=dotenv-key\n', encoding='utf-8')
        monkeypatch.setenv('GEMINI_API_KEY', 'environment-key')

        # act
        settings = Settings()

        # assert
        assert settings.gemini_api_key == 'environment-key'